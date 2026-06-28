from app.services.docker_service import create_workspace_container

result = create_workspace_container("demo-project")

print(result)