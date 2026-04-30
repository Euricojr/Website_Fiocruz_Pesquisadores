"""
team.py - Router for managing team members.
Handles CRUD operations for team members by interacting with Jekyll's YAML files.
"""
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_team_members():
    """Retrieve a list of all team members."""
    pass
