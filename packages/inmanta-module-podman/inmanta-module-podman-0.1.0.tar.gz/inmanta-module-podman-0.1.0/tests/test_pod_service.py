"""
    Copyright 2023 Guillaume Everarts de Velp

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Contact: edvgui@gmail.com
"""

from pytest_inmanta.plugin import Project


def test_model(project: Project) -> None:
    model = """
        import podman
        import podman::container_like
        import podman::container
        import podman::services
        import std

        user = std::get_env("USER")

        host = std::Host(
            name="localhost",
            remote_agent=true,
            remote_user=user,
            ip="127.0.0.1",
            os=std::linux,
        )

        pod = podman::Pod(
            host=host,
            name="inmanta-orchestrator",
            hostname=pod.name,
            owner=user,
            networks=[
                BridgeNetwork(
                    name="test-net",
                    ip=std::ipindex("172.42.0.0/24", position=3),
                ),
            ],
            publish=[
                Publish(
                    host_port="127.0.0.1:8888",
                    container_port="8888",
                ),
            ],
            uidmap=[
                IdMap(container_id="993", host_id="@1000"),
            ],
            gidmap=[
                IdMap(container_id="993", host_id="@1000"),
            ],
            containers=[
                podman::Container(
                    host=host,
                    name=f"{pod.name}-server",
                    image="ghcr.io/inmanta/orchestrator:latest",
                    owner=user,
                    user="993:993",
                    entrypoint="/usr/bin/inmanta",
                    command="-vvv --timed-logs server",
                ),
            ],
        )

        podman::services::SystemdPod(
            pod=pod,
            state="stopped",
            enabled=true,
        )
    """

    project.compile(model, no_dedent=False)
