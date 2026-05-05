"""
publications.py - Router for managing publications.
Handles CRUD operations for publications by interacting with Jekyll's YAML files.
"""
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional
from auth import get_current_user
from services.yaml_service import read_yaml, write_yaml
from services.build import rebuild_site
from services.sync_service import sync_publications

router = APIRouter()
FILENAME = "publications.yml"

class Publication(BaseModel):
    title: str
    authors: str
    year: str
    venue: str
    venue_type: str
    category: str
    link_url: Optional[str] = ""
    link_text: Optional[str] = ""

@router.get("/")
def get_publications(user: dict = Depends(get_current_user)):
    """Retrieve a list of all publications."""
    return read_yaml(FILENAME)

@router.post("/")
def add_publication(pub: Publication, user: dict = Depends(get_current_user)):
    """Add a publication, save YAML and rebuild site."""
    data = read_yaml(FILENAME)
    data.append(pub.model_dump() if hasattr(pub, 'model_dump') else pub.dict())
    write_yaml(FILENAME, data)
    rebuild = rebuild_site()
    return {"success": True, "message": "Publication added successfully", "rebuild": rebuild}

@router.delete("/{index}")
def delete_publication(index: int, user: dict = Depends(get_current_user)):
    """Remove a publication by index, save and rebuild."""
    data = read_yaml(FILENAME)
    if index < 0 or index >= len(data):
        raise HTTPException(status_code=404, detail="Publication not found")
    data.pop(index)
    write_yaml(FILENAME, data)
    rebuild = rebuild_site()
    return {"success": True, "message": "Publication deleted successfully", "rebuild": rebuild}

@router.post("/sync")
def sync_latest_publications(user: dict = Depends(get_current_user)):
    """Trigger sync from Google Scholar and rebuild site."""
    result = sync_publications()
    rebuild = None
    if result.get("success") and result.get("new_count", 0) > 0:
        rebuild = rebuild_site()
    
    return {
        "success": result.get("success"),
        "message": result.get("message") or f"{result.get('new_count')} novas publicações sincronizadas.",
        "details": result,
        "rebuild": rebuild
    }
