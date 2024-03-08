from __future__ import annotations

import datetime
import io
import json
import os
import pathlib
import shlex
import sys
from typing import List, Optional, Sequence

import click
import dask.config
import fabric
import invoke
from dask.base import tokenize
from dask.utils import parse_timedelta
from paramiko.ed25519key import Ed25519Key
from rich import print

import coiled
from coiled.spans import span
from coiled.utils import error_info_for_tracking, unset_single_thread_defaults

from ..v2.widgets.rich import LightRichClusterWidget
from .utils import CONTEXT_SETTINGS

# This directory is used by shell scripts that wrap the user's command
# Note that this directory is also referenced in code that runs in our
# cloud_env image, so if it's changed here, that code should also be updated.
COMMAND_DIR = "/scratch/run"


class KeepaliveSession:
    def __init__(self, cluster, prefix=""):
        self.cluster = cluster
        rand_uuid = coiled.utils.short_random_string()
        self.session_id = f"{prefix}-{rand_uuid}" if prefix else rand_uuid

    def __enter__(self):
        # keepalive session lets us use keepalive without dask client
        self.cluster._call_scheduler_comm("coiled_add_keepalive_session", name=self.session_id)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cluster._call_scheduler_comm("coiled_end_keepalive_session", name=self.session_id)


def get_ssh_connection(cloud, cluster_id):
    ssh_info = cloud.get_ssh_key(cluster_id=cluster_id)

    with io.StringIO(ssh_info["private_key"]) as f:
        pkey = Ed25519Key(file_obj=f)

    connection = fabric.connection.Connection(
        ssh_info["scheduler_public_address"], user="ubuntu", connect_kwargs={"pkey": pkey}
    )

    return connection


def write_via_ssh(connection, content, path, mode=None):
    with io.StringIO(content) as f:
        connection.put(f, path)
    if mode:
        connection.sftp().chmod(path, mode)


def upload_file(connection, f):
    cwd = os.path.abspath(os.path.curdir)
    is_under_cwd = os.path.commonpath((os.path.abspath(f), cwd)) == cwd

    if is_under_cwd:
        # For file that's inside cwd, keep the relative path.
        # Note that this could be different from how you specified the path, for example
        #   cwd=/foo/bar
        #   coiled run --file /foo/bar/nested/path.txt
        # file will be copied to /scratch/nested/path.txt
        # which is a little confusing, but means it's equivalent to
        #   coiled run --file ~/nested/path.txt
        # which does feel natural.
        specified_path_dir = os.path.dirname(os.path.relpath(f))
        remote_dir = f"/scratch/{specified_path_dir}/"
        make_remote_dir(connection, remote_dir)
    else:
        # for file outside cwd, ignore local path and put file directly in /scratch/
        remote_dir = "/scratch/"

    connection.put(f, remote_dir)


def run_via_ssh(cloud, cluster, info, command, file, env, skip_entrypoint: bool, interactive: bool, detach: bool):
    connection = get_ssh_connection(cloud, cluster.cluster_id)
    results = None

    original_command = shlex.join(command)
    callstack = [{"code": original_command, "relative_line": 0}]
    # Extract and upload files from `command`
    command = shlex.split(original_command)
    info["files-implicit"] = []  # implicit files are part of the command, e.g., `foo.py` in `coiled run python foo.py`
    for idx, i in enumerate(command):
        if os.path.exists(i) and os.path.isfile(i):
            # flatten paths, everything will be /scratch/foo
            # without any subdirectories
            connection.put(i, "/scratch/")
            info["files-implicit"].append(i)
            # adjust command to reference path on VM
            command[idx] = f"/scratch/{os.path.basename(i)}"

            # include code files in the "callstack"
            if i.endswith((".py", ".sh")):
                try:
                    with open(i) as f:
                        contents = f.read()
                    callstack.append({"code": contents, "filename": i})
                except Exception:
                    pass

    # Upload user-specified files too
    info["files-explicit"] = file
    for f in file:
        path = pathlib.Path(f)
        if not path.exists():
            raise FileNotFoundError(f"Cannot find specified file {f}")

        if path.is_file():
            upload_file(connection, path)
        elif path.is_dir():
            for subfile in path.rglob("*"):
                if subfile.is_file():
                    upload_file(connection, subfile)

    command_string = " ".join(command)

    container_name = "tmp-dask-1"

    if skip_entrypoint:
        entrypoint = ""
    else:
        entrypoint = get_entrypoint(connection, container_name)
        if "cloud-env" in entrypoint:
            # hack for cloud-env containers (e.g., package sync) currently required to avoid re-downloading senv
            # once container is suitably changed, we should just be able to use entrypoint like any other container
            entrypoint = "micromamba run -p /opt/coiled/env"

    docker_opts = "-it" if interactive else ""
    docker_opts = f"{docker_opts} --detach" if detach else docker_opts

    env_opts = " ".join(f"--env {key}={val}" for key, val in env.items()) if env else ""

    if not interactive:
        command_id = (
            f"{datetime.datetime.now(tz=datetime.timezone.utc).isoformat()}_{coiled.utils.short_random_string()}"
        )

        inner_command_path = f"{COMMAND_DIR}/{command_id}.sh"
        tee_command = f"{COMMAND_DIR}/{command_id}-tee.sh"

        make_remote_dir(connection, COMMAND_DIR)

        # write the user's command as a shell file
        write_via_ssh(connection, command_string, inner_command_path, mode=0o755)
        # wrapper file that calls user command, sending output to pseudo-tty and stdout (which goes into logs)
        escaped_original_command = original_command.replace('"', '"')
        tee_script = f"""
echo "{escaped_original_command}\t{command_id}" >> {COMMAND_DIR}/list
{inner_command_path} 2>&1 | tee -a /proc/1/fd/1
"""
        write_via_ssh(connection, tee_script, tee_command, mode=0o755)
        command_string = f"bash {tee_command}"

    container_command = (
        f"docker exec --workdir /scratch {env_opts} {docker_opts} {container_name} {entrypoint} {command_string}"
    )
    try:
        with KeepaliveSession(cluster=cluster, prefix="ssh"), span(cluster, callstack=callstack):
            results = connection.run(container_command, hide=not interactive, pty=interactive)
    except invoke.exceptions.UnexpectedExit as e:
        results = str(e)
    except Exception as e:
        raise e

    return connection, container_command, results


def make_remote_dir(connection, dir):
    connection.run(f"mkdir -p {dir} && sudo chmod a+wrx {dir}")


def get_entrypoint(connection, container_name) -> str:
    entrypoint = ""
    x = connection.run(f"docker inspect -f '{{{{json .Config.Entrypoint}}}}' {container_name}", hide=True)
    if x.stdout:
        entrypoint = json.loads(x.stdout)

        if entrypoint:
            # hack so we don't use `tini` for each run, remove everything between `tini` and `--`
            # e.g., "tini -g -- /usr/bin/prepare.sh" -> "/usr/bin/prepare.sh"
            if "tini" in entrypoint[0]:
                if "--" in entrypoint:
                    after_tini = entrypoint.index("--")
                    entrypoint = entrypoint[after_tini + 1 :]

            entrypoint = " ".join(entrypoint) if entrypoint else ""
    return entrypoint or ""


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option(
    "--name",
    default=None,
    help="Run name. If not given, defaults to a unique name.",
)
@click.option(
    "--account",
    "--workspace",
    default=None,
    help="Coiled workspace (uses default workspace if not specified)."
    " Note: --account is deprecated, please use --workspace instead.",
)
@click.option(
    "--software",
    default=None,
    help=(
        "Software environment name to use. If neither software nor container is specified, "
        "all the currently-installed Python packages are replicated on the VM using package sync."
    ),
)
@click.option(
    "--container",
    default=None,
    help=(
        "Container image to use. If neither software nor container is specified, "
        "all the currently-installed Python packages are replicated on the VM using package sync."
    ),
)
@click.option(
    "--vm-type",
    default=[],
    multiple=True,
    help="VM type to use. Specify multiple times to provide multiple options.",
)
@click.option(
    "--gpu",
    default=False,
    is_flag=True,
    help="Have a GPU available.",
)
@click.option(
    "--region",
    default=None,
    help="The cloud provider region in which to run the notebook.",
)
@click.option(
    "--disk-size",
    default=None,
    help="Use larger-than-default disk on VM, specified in GiB.",
)
@click.option(
    "--keepalive",
    default=None,
    help=(
        "Keep your VM running for the specified time, even after your command completes. "
        "In seconds (`--keepalive 60`) unless you specify units (`--keepalive 3m` for 3 minutes)."
        "Default to shutdown immediately after the command finishes."
    ),
)
@click.option(
    "--file",
    "-f",
    default=[],
    multiple=True,
    help="Local files required to run command.",
)
@click.option(
    "--env",
    "-e",
    default=[],
    multiple=True,
    help=(
        "Environment variables securely transmitted to run command environment. "
        "Format is `KEY=val`, multiple vars can be set with separate `--env` for each."
    ),
)
@click.option("--subdomain", default=None, help="Custom subdomain for the VM hostname.")
@click.option(
    "--allow-ssh-from",
    default="me",
    type=str,
    help=(
        "IP address or CIDR from which connections to port 22 (SSH) are open; "
        "can also be specified as 'everyone' (0.0.0.0/0) or 'me' (automatically determines public IP detected "
        "for your local client). Note that `coiled run` relies on SSH connection for executing commands on VM."
    ),
)
@click.option(
    "--port",
    default=[],
    type=int,
    multiple=True,
    help=(
        "Open extra ports in network firewall for inbound connections "
        "(multiple ports can be set with separate `--port` for each)."
    ),
)
@click.option(
    "--interactive",
    "-it",
    default=False,
    is_flag=True,
    help="Open an interactive session, e.g., `coiled run --interactive bash` or `coiled run --interactive python`.",
)
@click.option("--detach", default=False, is_flag=True, help="Start the run, don't wait for the results.")
@click.option(
    "--skip-entrypoint",
    default=False,
    is_flag=True,
    hidden=True,
)
@click.option(
    "--tag",
    "-t",
    default=[],
    multiple=True,
    help=("Tags. Format is `KEY=val`, multiple vars can be set with separate `--tag` for each."),
)
@click.argument("command", nargs=-1)
def run(
    name: str,
    account: Optional[str],
    software: Optional[str],
    container: Optional[str],
    vm_type: Sequence[str],
    gpu: bool,
    region: Optional[str],
    disk_size: Optional[int],
    keepalive,
    file,
    env,
    interactive: bool,
    subdomain: Optional[str],
    allow_ssh_from: str,
    port: List[int],
    detach: bool,
    skip_entrypoint: bool,
    tag,
    command,
):
    """
    Run a command on the cloud.
    """
    start_run(
        name=name,
        workspace=account,
        software=software,
        container=container,
        vm_type=vm_type,
        gpu=gpu,
        region=region,
        disk_size=disk_size,
        keepalive=keepalive,
        file=file,
        env=env,
        tag=tag,
        interactive=interactive,
        detach=detach,
        skip_entrypoint=skip_entrypoint,
        command=command,
        subdomain=subdomain,
        open_extra_ports=port,
        allow_ssh_from=allow_ssh_from,
    )


def start_run(
    name: str,
    workspace: Optional[str],
    software: Optional[str],
    container: Optional[str],
    vm_type: Sequence[str],
    gpu: bool,
    region: Optional[str],
    disk_size: Optional[int],
    keepalive,
    file,
    env,
    tag,
    interactive: bool,
    detach: bool,
    skip_entrypoint: bool,
    command,
    account: Optional[str] = None,
    idle_timeout: str = "24 hours",
    cluster_type_tag: str = "run/cli",
    subdomain: Optional[str] = None,
    open_extra_ports: Optional[List[int]] = None,
    allow_ssh_from: str = "me",
):
    runtime_env_dict = dict(env_var.split("=", maxsplit=1) for env_var in env)
    tags = dict(t.split("=", maxsplit=1) for t in tag)

    dask_env = unset_single_thread_defaults()
    if container and "rapidsai" in container:
        dask_env = {"DISABLE_JUPYTER": "true", **dask_env}  # needed for "stable" RAPIDS image

    if not command:
        raise ValueError("command must be specified")

    keepalive = parse_timedelta(keepalive)
    shutdown_on_close = keepalive is None

    info = {"command": command, "keepalive": keepalive, "subdomain": subdomain}
    success = True
    exception = None

    # if user tries `coiled run foo.py` they probably want to run `python foo.py` rather than `foo.py`
    if len(command) == 1 and command[0].endswith(".py"):
        command = ("python", command[0])

    connection = None
    container_command = None
    results = None

    try:
        with coiled.Cloud(workspace=workspace or account) as cloud:
            workspace = workspace or cloud.default_workspace
            with LightRichClusterWidget(
                workspace=workspace, title=f"Running [bold]{shlex.join(command)}[/bold]"
            ) as widget:
                widget.update(
                    server=cloud.server,
                    cluster_details=None,
                    logs=None,
                    workspace=workspace,
                )
                info["workspace"] = workspace
                cluster_kwargs = dict(
                    account=workspace,
                    n_workers=0,
                    software=software,
                    container=container,
                    scheduler_options={"idle_timeout": idle_timeout},
                    scheduler_vm_types=list(vm_type) if vm_type else None,
                    worker_vm_types=list(vm_type) if vm_type else None,
                    allow_ssh_from=allow_ssh_from,
                    open_extra_ports=open_extra_ports,
                    extra_worker_on_scheduler=True,
                    environ=dask_env,
                    scheduler_gpu=gpu,
                    region=region,
                    shutdown_on_close=shutdown_on_close,
                    tags={**tags, **{"coiled-cluster-type": cluster_type_tag}},
                    scheduler_disk_size=disk_size,
                    worker_disk_size=disk_size,
                    dashboard_custom_subdomain=subdomain,
                )
                token = tokenize(sys.executable, **cluster_kwargs)
                name = name or f"run-{token[:8]}"

                dask.config.set({"coiled.use_aws_creds_endpoint": True})
                with coiled.Cluster(name=name, cloud=cloud, custom_widget=widget, **cluster_kwargs) as cluster:
                    info["cluster_id"] = cluster.cluster_id

                    # set dask config so that cluster started from this cluster will re-use software env
                    runtime_env_dict["DASK_COILED__SOFTWARE"] = cluster._software_environment_name

                    if not shutdown_on_close:
                        cluster.set_keepalive(keepalive=keepalive)

                    if interactive:
                        widget.stop()

                    connection, container_command, results = run_via_ssh(
                        cloud=cloud,
                        cluster=cluster,
                        info=info,
                        command=command,
                        file=file,
                        interactive=interactive,
                        detach=detach,
                        skip_entrypoint=skip_entrypoint,
                        env=runtime_env_dict,
                    )

        if cluster.cluster_id and not interactive:
            if detach:
                print(f"Running [green]{shlex.join(command)}[/green] in background.")
            else:
                print()

                print("Output")
                print("-" * len("Output"))
                print()

            if results:
                if isinstance(results, str):
                    print(results)
                else:
                    print(results.stdout)
                    if results.stderr:
                        print(f"[red]{results.stderr}")

            print()

    except Exception as e:
        success = False
        exception = e
        raise e
    finally:
        coiled.add_interaction(
            "coiled-run-cli",
            success=success,
            **info,
            **error_info_for_tracking(exception),
        )
