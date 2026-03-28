from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse
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
    # Serve favicon.png as favicon.ico
    favicon_path = Path(__file__).parent / "favicon.png"
    if favicon_path.exists():
        return FileResponse(favicon_path, media_type="image/x-icon")
    # Fallback SVG if file not found
    return FileResponse(
        Path(__file__).parent / "favicon.png",
        media_type="image/png"
    )

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
