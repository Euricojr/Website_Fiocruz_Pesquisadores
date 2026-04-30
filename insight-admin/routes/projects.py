"""
projects.py - Router for managing projects.
Handles CRUD operations for projects by interacting with Jekyll's YAML files.
"""
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_projects():
    """Retrieve a list of all projects."""
    pass
