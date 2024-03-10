#!/usr/bin/env python3

import masoud


class Etcd(masoud.Service):
    name = "etcd"
    image = "github.com/satoqz/etcd"
    dockerfile = ("Dockerfile", ".")

    DEFAULT_CLIENT_PORT = 2379
    DEFAULT_PEER_PORT = 2380

    @property
    def ports(self) -> list[tuple[int, int]]:
        return [
            (
                self.host.get_var("etcd_client_port", int) or self.DEFAULT_CLIENT_PORT,
                self.DEFAULT_CLIENT_PORT,
            ),
            (
                self.host.get_var("etcd_peer_port", int) or self.DEFAULT_PEER_PORT,
                self.DEFAULT_PEER_PORT,
            ),
        ]

    DEFAULT_VOLUME_NAME = "example-etcd-data"
    VOLUME_MOUNT = "/data"

    @property
    def volumes(self) -> list[tuple[str, str]]:
        return [
            (
                self.host.get_var("etcd_volume", str) or self.DEFAULT_VOLUME_NAME,
                self.VOLUME_MOUNT,
            )
        ]

    DEFAULT_INITIAL_CLUSTER_TOKEN = "example-etcd-cluster"

    @property
    def command(self) -> list[str]:
        ip = self.host.must_get_var("ip", str)
        client_port = (
            self.host.get_var("etcd_client_port", int) or self.DEFAULT_CLIENT_PORT
        )

        initial_cluster_token = (
            self.host.get_var("etcd_initial_cluster_token", str)
            or self.DEFAULT_INITIAL_CLUSTER_TOKEN
        )
        initial_cluster = ",".join(
            f"{host.name}=http://{host.must_get_var("ip", str)}:{host.get_var("etcd_peer_port") or self.DEFAULT_PEER_PORT}"
            for host in self.group.get_hosts()
        )

        return [
            "etcd",
            f"--name={self.host.name}",
            f"--data-dir={self.VOLUME_MOUNT}/data",
            f"--wal-dir={self.VOLUME_MOUNT}/wal",
            f"--initial-advertise-peer-urls=http://{ip}:{self.DEFAULT_PEER_PORT}",
            f"--listen-peer-urls=http://0.0.0.0:{self.DEFAULT_PEER_PORT}",
            f"--listen-client-urls=http://0.0.0.0:{self.DEFAULT_CLIENT_PORT}",
            f"--advertise-client-urls=http://{ip}:{client_port}",
            f"--initial-cluster-token={initial_cluster_token}",
            f"--initial-cluster={initial_cluster}",
            "--initial-cluster-state=new",
        ]


if __name__ == "__main__":
    masoud.cli(services=[Etcd])
