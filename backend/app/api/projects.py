from app.services.docker_service import (
    create_workspace_container,
    delete_workspace_container,
)

from app.database.database import SessionLocal
from app.database.models import Project
from fastapi import APIRouter
from pydantic import BaseModel
import uuid
import os
import shutil
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

    # Open database session
    db = SessionLocal()

    # Create Project object
    project = Project(
        project_id=project_id,
        project_name=request.project_name,
        workspace=workspace_path,
        container_id=container["container_id"],
        status="created"
    )

    # Save to database
    db.add(project)
    db.commit()
    db.close()

    return {
        "project_id": project_id,
        "project_name": request.project_name,
        "workspace": workspace_path,
        "container": container,
        "status": "created"
    }

@router.get("/projects/{project_id}")
def get_project(project_id: str):

    db = SessionLocal()

    project = db.query(Project).filter(
        Project.project_id == project_id
    ).first()

    db.close()

    return project

@router.delete("/projects/{project_id}")
def delete_project(project_id: str):

    db = SessionLocal()

    project = db.query(Project).filter(
        Project.project_id == project_id
    ).first()

    if not project:
        db.close()
        return {"message": "Project not found"}

    # Delete Docker container
    delete_workspace_container(project.container_id)

    # Delete workspace folder
    if os.path.exists(project.workspace):
        shutil.rmtree(project.workspace)

    # Delete database record
    db.delete(project)
    db.commit()

    db.close()

    return {
        "message": "Project deleted successfully"
    }