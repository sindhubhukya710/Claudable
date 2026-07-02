import docker

client = docker.from_env()


def create_workspace_container(project_id: str):
    """
    Create a Docker container for a project.
    """

    container = client.containers.run(
        image="ubuntu:latest",
        name=f"claudable-{project_id}",
        command="sleep infinity",
        detach=True,
        tty=True,
        remove=False,
    )

    return {
        "container_id": container.id,
        "container_name": container.name,
        "status": container.status,
    }


def delete_workspace_container(container_id: str):
    """
    Stop and remove a Docker container.
    """

    try:
        container = client.containers.get(container_id)

        # Stop the container
        container.stop()

        # Remove the container
        container.remove()

        return {
            "status": "deleted"
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }