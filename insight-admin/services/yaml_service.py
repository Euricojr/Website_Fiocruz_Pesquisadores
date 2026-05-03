"""
yaml_service.py - Utility functions for reading and writing YAML files.
Used by the routers to edit the Jekyll data files directly on disk.
"""
import os
import yaml
from dotenv import load_dotenv

load_dotenv()

def get_file_path(filename: str) -> str:
    site_path = os.getenv("SITE_PATH")
    if not site_path:
        raise ValueError("SITE_PATH environment variable not set")
    return os.path.join(site_path, "_data", filename)

def read_yaml(filename: str):
    """Reads a YAML file and returns its contents as a dictionary or list."""
    file_path = get_file_path(filename)
    if not os.path.exists(file_path):
        return []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f) or []

def write_yaml(filename: str, data) -> bool:
    """Writes a dictionary or list to a YAML file."""
    file_path = get_file_path(filename)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        yaml.safe_dump(data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    return True
