from fastapi import FastAPI, UploadFile, File
from detector import detect_drones
import shutil
import os

app = FastAPI(
    title="Drone Detection API"
)

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.post("/detect")
async def detect(file: UploadFile = File(...)):

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = detect_drones(file_path)

    return result
