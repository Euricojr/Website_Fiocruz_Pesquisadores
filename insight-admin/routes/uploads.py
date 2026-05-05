"""
uploads.py - Router for managing file uploads.
Handles uploading and serving static assets like images and documents.
"""
import os
import uuid
import aiofiles
from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, status
from auth import get_current_user
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

SITE_PATH = os.getenv("SITE_PATH", "../Website_Fiocruz_Pesquisadores")
IMG_DIR = os.path.join(SITE_PATH, "assets", "img")
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "webp", "gif"}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB

# Ensure the upload directory exists
os.makedirs(IMG_DIR, exist_ok=True)

def is_allowed_extension(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@router.post("/image")
async def upload_image(file: UploadFile = File(...), current_user: dict = Depends(get_current_user)):
    """Upload a new image."""
    if not file.filename:
        raise HTTPException(status_code=400, detail="Nenhum arquivo enviado")
    
    if not is_allowed_extension(file.filename):
        raise HTTPException(status_code=400, detail="Formato de arquivo não suportado. Use JPG, JPEG, PNG, WEBP ou GIF.")
    
    # Read file content to check size
    contents = await file.read()
    if len(contents) > MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail="O arquivo excede o limite de 5MB.")
    
    # Generate unique filename: short UUID + original filename
    unique_filename = f"{uuid.uuid4().hex[:8]}-{file.filename}"
    
    file_path = os.path.join(IMG_DIR, unique_filename)
    
    # Save the file using aiofiles
    async with aiofiles.open(file_path, "wb") as out_file:
        await out_file.write(contents)
        
    return {
        "success": True,
        "url": f"/assets/img/{unique_filename}",
        "filename": unique_filename
    }

@router.get("/images")
async def list_images(current_user: dict = Depends(get_current_user)):
    """List all uploaded images."""
    if not os.path.exists(IMG_DIR):
        return []
    
    images = []
    for filename in os.listdir(IMG_DIR):
        if is_allowed_extension(filename):
            images.append({
                "filename": filename,
                "url": f"/assets/img/{filename}"
            })
    return images

@router.delete("/image/{filename}")
async def delete_image(filename: str, current_user: dict = Depends(get_current_user)):
    """Delete an image by filename."""
    if not is_allowed_extension(filename):
        raise HTTPException(status_code=400, detail="Extensão inválida para exclusão.")
        
    # Prevent directory traversal attacks
    if "/" in filename or "\\" in filename or ".." in filename:
        raise HTTPException(status_code=400, detail="Nome de arquivo inválido.")
        
    file_path = os.path.join(IMG_DIR, filename)
    
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Imagem não encontrada.")
        
    try:
        os.remove(file_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao deletar arquivo: {str(e)}")
        
    return {"success": True, "message": "Imagem deletada com sucesso"}
