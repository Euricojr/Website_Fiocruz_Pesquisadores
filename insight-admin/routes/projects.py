"""
projects.py - Router for managing projects.
Handles CRUD operations for projects by interacting with Jekyll's YAML files.
"""
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from auth import get_current_user
from services.yaml_service import read_yaml, write_yaml
from services.build import rebuild_site

router = APIRouter()
FILENAME = "projects.yml"

class Project(BaseModel):
    title: str
    description: str
    tags: List[str]
    image: Optional[str] = ""
    url: Optional[str] = ""

@router.get("/")
def get_projects(user: dict = Depends(get_current_user)):
    """Retrieve a list of all projects."""
    return read_yaml(FILENAME)

@router.post("/")
def add_project(project: Project, user: dict = Depends(get_current_user)):
    """Add a project, save YAML and rebuild site."""
    data = read_yaml(FILENAME)
    data.append(project.model_dump() if hasattr(project, 'model_dump') else project.dict())
    write_yaml(FILENAME, data)
    rebuild = rebuild_site()
    return {"success": True, "message": "Project added successfully", "rebuild": rebuild}

@router.delete("/{index}")
def delete_project(index: int, user: dict = Depends(get_current_user)):
    """Remove a project by index, save and rebuild."""
    data = read_yaml(FILENAME)
    if index < 0 or index >= len(data):
        raise HTTPException(status_code=404, detail="Project not found")
    data.pop(index)
    write_yaml(FILENAME, data)
    rebuild = rebuild_site()
    return {"success": True, "message": "Project deleted successfully", "rebuild": rebuild}
