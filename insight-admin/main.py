"""
main.py - Entry point for the INSIGHT Admin FastAPI application.
Configures CORS, static files serving, and registers routers for various endpoints.
"""
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv

from auth import router as auth_router
from routes.publications import router as publications_router
from routes.projects import router as projects_router
from routes.team import router as team_router
from routes.uploads import router as uploads_router
from database import init_db

load_dotenv()

# Initialize database
init_db()

app = FastAPI(title="INSIGHT Admin API", description="Backend for INSIGHT Jekyll site management")

# CORS configuration
allowed_origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000,http://127.0.0.1:3000,http://localhost:4000").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ensure static/admin/ directory exists before mounting
os.makedirs("static/admin", exist_ok=True)
# Serve static files for the admin panel UI
app.mount("/static/admin", StaticFiles(directory="static/admin"), name="admin_static")

# Mount Jekyll assets to serve images in the admin panel
SITE_PATH = os.getenv("SITE_PATH", "../Website_Fiocruz_Pesquisadores")
assets_path = os.path.join(SITE_PATH, "assets")
if os.path.exists(assets_path):
    app.mount("/assets", StaticFiles(directory=assets_path), name="site_assets")

# Register routers
app.include_router(auth_router, prefix="/api/auth", tags=["auth"])
app.include_router(publications_router, prefix="/api/publications", tags=["publications"])
app.include_router(projects_router, prefix="/api/projects", tags=["projects"])
app.include_router(team_router, prefix="/api/team", tags=["team"])
app.include_router(uploads_router, prefix="/api/uploads", tags=["uploads"])

@app.get("/api/health")
def health_check():
    return {"status": "ok"}
