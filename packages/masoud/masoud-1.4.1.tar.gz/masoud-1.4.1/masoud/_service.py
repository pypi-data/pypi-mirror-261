from ._inventory import Group, Host, Inventory


class Service:
    """A service describes how a certain docker container is built/run/stopped/...
    within the context of its host, group and inventory.
    """

    _host: Host

    @property
    def host(self) -> Host:
        """Reference to the host the service is being used with.
        This will be `localhost` during builds.
        """
        return self._host

    @property
    def group(self) -> Group:
        """Reference to the inventory group the service is being used with"""
        return self.host.group

    @property
    def inventory(self) -> Inventory:
        """Reference to the inventory the service is being used with"""
        return self.host.inventory

    def __init__(self, host: Host) -> None:
        self._host = host
        REQUIRED_ATTRS = ["name", "image"]
        for attr in REQUIRED_ATTRS:
            if getattr(self, attr, None) is None:
                raise ValueError(f"service is missing required attribute `{attr}`")

    name: str
    """The name of the service"""

    image: str
    """The tag of the container image used by the service"""

    docker: list[str] = ["docker"]
    """The base docker command and arguments before the first subcommand (you can also put `["podman"]` here)"""

    context: str | None = None
    """The docker context to use, see `docker --context`"""

    dockerfile: tuple[str, str] | None = None
    """Tuple of (Dockerfile, build path) to build service's image (Keep this empty to pull from a registry instead)"""

    container_name: str | None
    """Container name passed to see `docker run --name`"""

    init: bool = True
    """Pass the `--init` flag to `docker run`."""

    restart: str | None = "unless-stopped"
    """Restart option that is passed to `docker run --restart`"""

    ports: list[tuple[int | str, int | str]] = []
    """List of `(outer_port, inner_port)` mappings passed to `docker run -p`"""

    volumes: list[tuple[str, str]] = []
    """List of `(volume, mountpoint)` mappings passed to `docker run -v`"""

    networks: list[str] = []
    """List of networks passed to `docker run --network`"""

    command: list[str] = []
    """The command that is passed to the container"""

    stop_signal: str | None = None
    """Signal passed to `-s` argument of `docker stop`"""

    stop_timeout: str | None = None
    """Timeout passed to `-t` argument of `docker stop`"""

    extra_build_args: list[str] = []
    """Additional arguments passed to `docker build`"""

    extra_pull_args: list[str] = []
    """Additional arguments passed to `docker pull`"""

    extra_run_args: list[str] = []
    """Additional arguments passed to `docker run`"""
