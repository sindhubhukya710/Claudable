from app.services.docker_service import create_workspace_container
from fastapi import APIRouter
from pydantic import BaseModel
import uuid
import os

router = APIRouter()


class ProjectRequest(BaseModel):
    project_name: str


@router.post("/projects")
def create_project(request: ProjectRequest):

    project_id = str(uuid.uuid4())

    workspace_path = os.path.join(
        "workspaces",
        project_id
    )

    os.makedirs(workspace_path, exist_ok=True)

    # Create a Docker container for this project
    container = create_workspace_container(project_id)

    return {
        "project_id": project_id,
        "project_name": request.project_name,
        "workspace": workspace_path,
        "container": container,
        "status": "created"
    }