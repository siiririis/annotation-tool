from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, Response

import json

app = FastAPI()

app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/")
def serve_frontend():
    return FileResponse("frontend/index.html")

@app.get("/favicon.ico")
def favicon():
    return Response(status_code=204)

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    first_line = contents.decode("utf-8").splitlines()[0]
    document = json.loads(first_line)
    return document