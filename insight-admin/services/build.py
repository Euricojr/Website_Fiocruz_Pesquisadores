"""
build.py - Service for triggering Jekyll site builds.
Uses subprocess to execute the Jekyll build command in the configured site directory.
"""
import os
import subprocess
from dotenv import load_dotenv

load_dotenv()

def rebuild_site() -> dict:
    """
    Executes 'bundle exec jekyll build' inside the SITE_PATH directory.
    
    Returns:
        dict: A dictionary containing 'success' (boolean) and 'output' (string)
              with the stdout and stderr combined.
    """
    site_path = os.getenv("SITE_PATH")
    
    if not site_path or not os.path.exists(site_path):
        return {
            "success": False,
            "output": f"Error: SITE_PATH '{site_path}' is not configured or does not exist."
        }
        
    try:
        # Run bundle exec jekyll build
        result = subprocess.run(
            ["bundle", "exec", "jekyll", "build"],
            cwd=os.path.abspath(site_path),
            capture_output=True,
            text=True,
            check=False
        )
        
        success = result.returncode == 0
        output = result.stdout + "\n" + result.stderr
        
        return {
            "success": success,
            "output": output.strip()
        }
        
    except Exception as e:
        return {
            "success": False,
            "output": f"Exception occurred during build: {str(e)}"
        }
