import json
import subprocess
import sys

from ._logging import err, ok
from ._service import Service


def pull_image(svc: Service) -> None:
    """Pull the service's container image"""
    image = svc.image
    result = svc.host.run([*svc.docker, "pull", *svc.extra_pull_args, image])
    if result.returncode != 0:
        err(f'failed to pull image "{image}" on "{svc.host.name}"!')
        sys.exit(1)
    ok(f'pulled image "{image}" on "{svc.host.name}"')


def export_image(svc: Service) -> subprocess.Popen:
    """Export the service's container image to stdout"""
    return svc.host.popen(
        [*svc.docker, "save", svc.image],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def import_image(svc: Service, export: subprocess.Popen) -> None:
    """Import the service's container image from the stdout of another process"""
    result = svc.host.run(
        [*svc.docker, "load"], capture_output=True, text=True, stdin=export.stdout
    )
    export_returncode = export.wait()
    if result.returncode + export_returncode != 0:
        err(
            f'failed to import image "{svc.image}" on "{svc.host.name}"!',
            export.stderr.read()
            if export_returncode != 0 and export.stderr is not None
            else None,
            result.stderr if export.returncode != 0 else None,
        )
        sys.exit(1)
    ok(f'imported image {svc.image} on "{svc.host.name}"')


def build_image(svc: Service) -> None:
    """Build the service's container image"""
    assert svc.dockerfile is not None
    command = [
        *svc.docker,
        "build",
        f"-t={svc.image}",
        f"-f={svc.dockerfile[0]}",
        *svc.extra_build_args,
        svc.dockerfile[1],
    ]
    result = svc.host.run(command)
    if result.returncode != 0:
        err(f'failed to build image "{svc.image}" for service "{svc.name}"')
        sys.exit(1)
    ok(f'built image for service "{svc.name}"')


def inspect_container(svc: Service) -> list[dict]:
    """Inspect the service's container"""
    result = svc.host.run(
        [*svc.docker, "inspect", svc.container_name or svc.name],
        capture_output=True,
        text=True,
    )
    try:
        return json.loads(result.stdout)
    except Exception:
        err(
            f'failed to inspect container "{svc.container_name or svc.name}" on "{svc.host.name}"',
            result.stderr,
        )
        sys.exit(1)


def check_running(svc: Service) -> bool:
    """Check if the service's container is running"""
    inspection = inspect_container(svc)
    return (
        len(inspection) > 0
        and "State" in inspection[0]
        and isinstance(inspection[0]["State"], dict)
        and inspection[0]["State"]["Status"] == "running"
    )


def start_container(svc: Service) -> None:
    """Start the service's container"""
    command = [
        *svc.docker,
        "run",
        "-d",
        f"--name={svc.container_name or svc.name}",
        *(["--init"] if svc.init else []),
        *(
            [f"--restart={restart}"]
            if ((restart := svc.restart) not in [None, "no"])
            else []
        ),
        *[f"-p={outer_port}:{inner_port}" for outer_port, inner_port in svc.ports],
        *[
            f"-v={outer_mount}:{inner_mount}"
            for outer_mount, inner_mount in svc.volumes
        ],
        *[f"--network={network}" for network in svc.networks],
        *svc.extra_run_args,
        svc.image,
        *svc.command,
    ]
    result = svc.host.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        err(f'failed to start "{svc.name}" on "{svc.host.name}"!', result.stderr)
        sys.exit(1)
    ok(f'started service "{svc.name}" on "{svc.host.name}"')


def stop_container(svc: Service) -> None:
    """Stop the service's container"""
    command = [
        *svc.docker,
        "stop",
        *([f"-s={signal}"] if (signal := svc.stop_signal) is not None else []),
        *([f"-t={timeout}"] if (timeout := svc.stop_timeout) is not None else []),
        svc.container_name or svc.name,
    ]
    result = svc.host.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        err(
            f'failed to stop service "{svc.name}" on "{svc.host.name}"!',
            result.stderr,
        )
        sys.exit(1)
    ok(f'stopped service "{svc.name}" on "{svc.host.name}"')


def remove_container(svc: Service) -> None:
    """Remove the service's container"""
    inspection = inspect_container(svc)
    if len(inspection) < 1:
        return
    result = svc.host.run(
        [*svc.docker, "rm", svc.container_name or svc.name],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        err(
            f'failed to remove container "{svc.container_name or svc.name}" on "{svc.host.name}"',
            result.stderr,
        )
        sys.exit(1)
    ok(f'removed container "{svc.container_name or svc.name}" on "{svc.host.name}"')


def view_logs(svc: Service, follow: bool = False) -> None:
    """View the service's container's logs"""
    command = [
        *svc.docker,
        "logs",
        *(["-f"] if follow else []),
        svc.container_name or svc.name,
    ]
    result = svc.host.run(command)
    if result.returncode != 0:
        err(f'Failed to show logs for "{svc.name}" on "{svc.host.name}"!')
        sys.exit(1)
