import os

from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import FileResponse

from auto_artifacts.server.config import BASE_PATH
from auto_artifacts.server.auth import authenticate
from auto_artifacts.server.log import get_logger

router = APIRouter()

logger = get_logger(__name__)

@router.get("/file")
def download(filename: str = Query(..., description="The name of the file to download"),
             path: str = Query(..., description="The path to the file, relative to the base path"),
             pw: str = Query(None, description="Password for accessing private files")):

    full_path = os.path.join(BASE_PATH, path)
    if not os.path.exists(full_path):
        raise HTTPException(status_code=404, detail="Invalid file or path")

    if "private" in path:
        if not authenticate(pw):
            raise HTTPException(status_code=401, detail="Protected access.")

    file_path = os.path.join(full_path, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File does not exist")
    logger.info(f"Downloaded: {file_path}")

    return FileResponse(path=file_path, filename=filename, media_type='application/octet-stream')
