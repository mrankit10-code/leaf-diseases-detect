from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, Response, FileResponse
from fastapi.staticfiles import StaticFiles
import logging
import os
from pathlib import Path
from utils import convert_image_to_base64_and_test

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Leaf Disease Detection API", version="2.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/favicon.ico")
async def favicon():
    # Return a simple SVG favicon
    svg = b'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><rect fill="#1b5e20" width="100" height="100"/><text x="50" y="70" font-size="60" font-weight="bold" fill="white" text-anchor="middle" font-family="Arial">🌿</text></svg>'
    return Response(content=svg, media_type="image/svg+xml")

@app.post('/disease-detection-file')
async def disease_detection_file(file: UploadFile = File(...)):
    try:
        logger.info(f"Received: {file.filename}")
        
        if file.content_type not in ['image/jpeg', 'image/jpg', 'image/png']:
            raise HTTPException(status_code=400, detail="Invalid file type")
        
        contents = await file.read()
        
        if len(contents) > 5 * 1024 * 1024:
            raise HTTPException(status_code=413, detail="File too large")
        
        result = convert_image_to_base64_and_test(contents)
        
        if result is None:
            raise HTTPException(status_code=500, detail="Processing failed")
        
        return JSONResponse(content=result)
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "API Online", "version": "2.0.0"}

@app.get("/health")
async def health():
    return {"status": "healthy"}
