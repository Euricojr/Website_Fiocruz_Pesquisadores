"""
team.py - Router for managing team members.
Handles CRUD operations for team members by interacting with Jekyll's YAML files.
"""
from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from pydantic import BaseModel
from typing import Optional
from auth import get_current_user
from services.yaml_service import read_yaml, write_yaml
from services.build import rebuild_site

router = APIRouter()
FILENAME = "team.yml"

class TeamMember(BaseModel):
    category: str
    name: str
    role: str
    institution: Optional[str] = ""
    image: Optional[str] = ""
    lattes: Optional[str] = ""
    linkedin: Optional[str] = ""

@router.get("/")
def get_team_members(user: dict = Depends(get_current_user)):
    """Retrieve a list of all team members."""
    return read_yaml(FILENAME)

@router.post("/member")
def add_team_member(member: TeamMember, background_tasks: BackgroundTasks, user: dict = Depends(get_current_user)):
    """Add a team member to an existing category, save and rebuild site."""
    data = read_yaml(FILENAME)
    
    # Find the category
    category_found = False
    for cat in data:
        if cat.get("category") == member.category:
            if "members" not in cat:
                cat["members"] = []
            
            member_dict = member.model_dump(exclude={"category"}) if hasattr(member, 'model_dump') else member.dict(exclude={"category"})
            cat["members"].append(member_dict)
            category_found = True
            break
            
    if not category_found:
        # Automatically create the new category instead of raising 404
        member_dict = member.model_dump(exclude={"category"}) if hasattr(member, 'model_dump') else member.dict(exclude={"category"})
        data.append({"category": member.category, "members": [member_dict]})
        
    write_yaml(FILENAME, data)
    background_tasks.add_task(rebuild_site)
    return {"success": True, "message": "Membro da equipe adicionado. O site está sendo reconstruído em segundo plano."}

@router.delete("/member/{category_index}/{member_index}")
def delete_team_member(category_index: int, member_index: int, background_tasks: BackgroundTasks, user: dict = Depends(get_current_user)):
    """Remove a member by category index and member index, save and rebuild."""
    data = read_yaml(FILENAME)
    
    if category_index < 0 or category_index >= len(data):
        raise HTTPException(status_code=404, detail="Category index not found")
        
    category = data[category_index]
    if "members" not in category or member_index < 0 or member_index >= len(category["members"]):
        raise HTTPException(status_code=404, detail="Member index not found in category")
        
    category["members"].pop(member_index)
    
    write_yaml(FILENAME, data)
    background_tasks.add_task(rebuild_site)
    return {"success": True, "message": "Membro da equipe removido. O site está sendo reconstruído em segundo plano."}
