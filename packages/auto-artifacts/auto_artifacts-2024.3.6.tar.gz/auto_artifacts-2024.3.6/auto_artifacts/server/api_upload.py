import os
from typing import List

from fastapi import UploadFile, File, HTTPException, Form, APIRouter

from auto_artifacts.server.auth import authenticate
from auto_artifacts.server.config import BASE_PATH
from auto_artifacts.server.log import get_logger

router = APIRouter()

logger = get_logger(__name__)

@router.post("/files")
async def upload(files: List[UploadFile] = File(...), path: str = Form(...), pw: str = Form(...)):
    full_path = os.path.join(BASE_PATH, path)
    if not os.path.exists(full_path):
        os.makedirs(full_path)

    if "private" in path:
        if not authenticate(pw):
            raise HTTPException(status_code=401, detail="Protected access.")

    for file in files:
        file_location = os.path.join(full_path, file.filename)
        with open(file_location, "wb+") as file_object:
            file_object.write(await file.read())
        logger.info(f"Uploaded: {file_location}")

    return {"message": "File(s) uploaded successfully."}
