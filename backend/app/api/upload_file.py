import os
from fastapi import APIRouter, UploadFile, HTTPException
from pathlib import Path
import shutil

from .store_faiss_embeddings import save_faiss_embeddings_file

file_upload_path = os.path.join(Path(__file__).parent.parent, "Uploads")
embeddings_upload_path = os.path.join(Path(__file__).parent.parent, "Embeddings")
Path(file_upload_path).mkdir(parents=True, exist_ok=True)
Path(embeddings_upload_path).mkdir(parents=True, exist_ok=True)


ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx', 'txt', 'csv'}
def is_allowed_file(filename: str) -> bool:
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

upload_router = APIRouter()


@upload_router.post("/upload_process_file", description="Upload the file to chat and save its embeddings")
async def upload_file_create_embeddings(file: UploadFile):
    if not is_allowed_file(file.filename):
        raise HTTPException(status_code=400, detail="File type not allowed")
    
    # Save the file.
    file_save_path = os.path.join(file_upload_path, file.filename)
    if not os.path.exists(file_save_path):
        with open(file_save_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Save the embeddings
        save_faiss_embeddings_file(file_path=file_save_path, 
                                embeddings_folder_path=embeddings_upload_path)

        return {"filename": file.filename, "status": "File and embeddings uploaded successfully"}
    else:
        return {"filename": file.filename, "status": "File and embeddings already exists"}