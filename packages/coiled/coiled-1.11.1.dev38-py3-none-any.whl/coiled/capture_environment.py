import asyncio
import logging
import platform
import typing
from logging import getLogger
from typing import Dict, List, Optional, Set, Tuple, cast

from rich.progress import Progress
from typing_extensions import Literal

from coiled.context import track_context
from coiled.scan import scan_prefix
from coiled.software_utils import (
    check_pip_happy,
    create_wheels_for_local_python,
    create_wheels_for_packages,
    partition_ignored_packages,
    partition_local_packages,
    partition_local_python_code_packages,
)
from coiled.types import ArchitectureTypesEnum, PackageInfo, PackageLevelEnum, ResolvedPackageInfo
from coiled.v2.core import CloudV2
from coiled.v2.widgets.util import simple_progress

PYTHON_VERSION = platform.python_version_tuple()
ANY_AVAILABLE = "ANY-AVAILABLE"


logger = getLogger("coiled.package_sync")


async def default_python() -> PackageInfo:
    python_version = platform.python_version()
    return {
        "name": "python",
        "path": None,
        "source": "conda",
        "channel_url": ANY_AVAILABLE,
        "channel": ANY_AVAILABLE,
        "subdir": "linux-64",
        "conda_name": "python",
        "version": python_version,
        "wheel_target": None,
    }


@track_context
async def approximate_packages(
    cloud: CloudV2,
    packages: List[PackageInfo],
    priorities: Dict[Tuple[str, Literal["conda", "pip"]], PackageLevelEnum],
    progress: Optional[Progress] = None,
    strict: bool = False,
    architecture: ArchitectureTypesEnum = ArchitectureTypesEnum.X86_64,
    pip_check_errors: Optional[Dict[str, List[str]]] = None,
) -> typing.List[ResolvedPackageInfo]:
    user_conda_installed_python = next((p for p in packages if p["name"] == "python"), None)
    user_conda_installed_pip = next(
        (i for i, p in enumerate(packages) if p["name"] == "pip" and p["source"] == "conda"),
        None,
    )
    if not user_conda_installed_pip:
        # This means pip was installed by pip, or the system
        # package manager
        # Insert a conda version of pip to be installed first, it will
        # then be used to install the users version of pip
        pip = next(
            (p for p in packages if p["name"] == "pip" and p["source"] == "pip"),
            None,
        )
        if not pip:
            # insert a modern version and hope it does not introduce conflicts
            packages.append({
                "name": "pip",
                "path": None,
                "source": "conda",
                "channel_url": "https://conda.anaconda.org/conda-forge/",
                "channel": "conda-forge",
                "subdir": "noarch",
                "conda_name": "pip",
                "version": "22.3.1",
                "wheel_target": None,
            })
        else:
            # insert the users pip version and hope it exists on conda-forge
            packages.append({
                "name": "pip",
                "path": None,
                "source": "conda",
                "channel_url": "https://conda.anaconda.org/conda-forge/",
                "channel": "conda-forge",
                "subdir": "noarch",
                "conda_name": "pip",
                "version": pip["version"],
                "wheel_target": None,
            })
    coiled_selected_python = None
    if not user_conda_installed_python:
        # insert a special python package
        # that the backend will pick a channel for
        coiled_selected_python = await default_python()
        packages.append(coiled_selected_python)
    packages, _ = partition_ignored_packages(packages, priorities=priorities)
    packages, local_python_code = partition_local_python_code_packages(packages)
    packages, local_python_wheel_packages = partition_local_packages(packages)
    with simple_progress("Validating environment", progress=progress):
        results = await cloud._approximate_packages(
            packages=[
                {
                    "name": pkg["name"],
                    "priority_override": (
                        PackageLevelEnum.CRITICAL
                        if (
                            strict
                            or (
                                pkg["wheel_target"]
                                # Ignore should override wheel_target (see #2640)
                                and not priorities.get((pkg["name"], pkg["source"])) == PackageLevelEnum.IGNORE
                            )
                        )
                        else priorities.get((
                            (cast(str, pkg["conda_name"]) if pkg["source"] == "conda" else pkg["name"]),
                            pkg["source"],
                        ))
                    ),
                    "python_major_version": PYTHON_VERSION[0],
                    "python_minor_version": PYTHON_VERSION[1],
                    "python_patch_version": PYTHON_VERSION[2],
                    "source": pkg["source"],
                    "channel_url": pkg["channel_url"],
                    "channel": pkg["channel"],
                    "subdir": pkg["subdir"],
                    "conda_name": pkg["conda_name"],
                    "version": pkg["version"],
                    "wheel_target": pkg["wheel_target"],
                }
                for pkg in packages
            ],
            architecture=architecture,
            pip_check_errors=pip_check_errors,
        )
    result_map = {(r["name"], r["conda_name"]): r for r in results}
    finalized_packages: typing.List[ResolvedPackageInfo] = []

    if not user_conda_installed_python and coiled_selected_python:
        # user has no python version installed by conda
        # we should have a result of asking the backend to
        # pick conda channel that has the users python version
        python_result = result_map[("python", "python")]
        if result_map[("python", "python")]["error"]:
            finalized_packages.append({
                "name": "python",
                "source": "conda",
                "channel": None,
                "conda_name": "python",
                "client_version": coiled_selected_python["version"],
                "specifier": python_result["specifier"] or "",
                "include": python_result["include"],
                "note": None,
                "error": python_result["error"],
                "sdist": None,
                "md5": None,
            })
        else:
            note = python_result["note"]
            if not note:
                raise ValueError("Expected a note from the backend")
            channel_url, channel = note.split(",")
            finalized_packages.append({
                "name": "python",
                "source": "conda",
                "channel": channel,
                "conda_name": "python",
                "client_version": coiled_selected_python["version"],
                "specifier": python_result["specifier"] or "",
                "include": python_result["include"],
                "note": None,
                "error": python_result["error"],
                "sdist": None,
                "md5": None,
            })
        # we can pull our special python package out of the list
        # now
        packages.remove(coiled_selected_python)
    finalized_packages.extend(await create_wheels_for_local_python(local_python_code, progress=progress))
    finalized_packages.extend(await create_wheels_for_packages(local_python_wheel_packages, progress=progress))
    for pkg in packages:
        package_result = result_map[(pkg["name"], pkg["conda_name"])]
        # Handle custom PyPI URLs
        if pkg["source"] == "pip" and package_result["include"] and package_result["note"]:
            finalized_packages.append({
                "name": pkg["name"],
                "source": pkg["source"],
                "channel": package_result["note"],
                "conda_name": pkg["conda_name"],
                "client_version": pkg["version"],
                "specifier": package_result["specifier"] or "",
                "include": package_result["include"],
                "note": None,
                "error": package_result["error"],
                "sdist": None,
                "md5": None,
            })
        else:
            finalized_packages.append({
                "name": pkg["name"],
                "source": pkg["source"],
                "channel": pkg["channel"],
                "conda_name": pkg["conda_name"],
                "client_version": pkg["version"],
                "specifier": package_result["specifier"] or "",
                "include": package_result["include"],
                "note": package_result["note"],
                "error": package_result["error"],
                "sdist": None,
                "md5": None,
            })
    return finalized_packages


@track_context
async def create_environment_approximation(
    cloud: CloudV2,
    priorities: Dict[Tuple[str, Literal["conda", "pip"]], PackageLevelEnum],
    only: Optional[Set[str]] = None,
    strict: bool = False,
    progress: Optional[Progress] = None,
    architecture: ArchitectureTypesEnum = ArchitectureTypesEnum.X86_64,
) -> typing.List[ResolvedPackageInfo]:
    packages = await scan_prefix(progress=progress)
    pip_check_errors = await check_pip_happy(progress)
    if only:
        packages = [pkg for pkg in packages if pkg["name"] in only]
    result = await approximate_packages(
        cloud=cloud,
        packages=[pkg for pkg in packages],
        priorities=priorities,
        strict=strict,
        progress=progress,
        architecture=architecture,
        pip_check_errors=pip_check_errors,
    )
    return result


if __name__ == "__main__":
    from logging import basicConfig

    basicConfig(level=logging.INFO)

    from rich.console import Console
    from rich.table import Table

    async def run():
        async with CloudV2(asynchronous=True) as cloud:
            return await create_environment_approximation(
                cloud=cloud,
                priorities={
                    ("dask", "conda"): PackageLevelEnum.CRITICAL,
                    ("twisted", "conda"): PackageLevelEnum.IGNORE,
                    ("graphviz", "conda"): PackageLevelEnum.LOOSE,
                    ("icu", "conda"): PackageLevelEnum.LOOSE,
                },
            )

    result = asyncio.run(run())

    table = Table(title="Packages")
    keys = ("name", "source", "include", "client_version", "specifier", "error", "note")

    for key in keys:
        table.add_column(key)

    for pkg in result:
        row_values = [str(pkg.get(key, "")) for key in keys]
        table.add_row(*row_values)
    console = Console()
    console.print(table)
    console.print(table)
