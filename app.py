from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse, Response
import logging
import os
from pathlib import Path
from utils import convert_image_to_base64_and_test, init_detector, get_detector

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

# Initialize detector on startup
@app.on_event("startup")
async def startup_event():
    """Initialize detector model on startup"""
    try:
        logger.info("Loading AI model on startup...")
        init_detector()
        logger.info("✅ Model loaded successfully!")
    except Exception as e:
        logger.error(f"⚠️ Model loading on startup failed (will retry on first request): {e}")

@app.get("/favicon.ico")
async def favicon():
    # Serve favicon.ico file
    favicon_path = Path(__file__).parent / "favicon.ico"
    if favicon_path.exists():
        return FileResponse(favicon_path, media_type="image/x-icon")
    return Response(status_code=204)

@app.get("/")
async def root():
    return {"message": "API Online", "version": "2.0.0"}

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.get("/warmup")
async def warmup():
    """Warmup endpoint to ensure model is loaded and ready"""
    try:
        detector = get_detector()
        if detector is None:
            init_detector()
        return {"status": "ready", "message": "Model is loaded and ready for inference"}
    except Exception as e:
        logger.error(f"Warmup failed: {e}")
        return {"status": "initializing", "message": "Model is initializing, please retry in a moment"}

@app.post('/disease-detection-file')
async def disease_detection_file(file: UploadFile = File(...)):
    try:
        logger.info(f"Received: {file.filename}")
        
        if file.content_type not in ['image/jpeg', 'image/jpg', 'image/png']:
            raise HTTPException(status_code=400, detail="Invalid file type")
        
        contents = await file.read()
        
        if len(contents) > 5 * 1024 * 1024:
            raise HTTPException(status_code=413, detail="File too large")
        
        logger.info("Processing image for disease detection...")
        result = convert_image_to_base64_and_test(contents)
        
        if result is None:
            raise HTTPException(status_code=500, detail="Processing failed")
        
        logger.info("✅ Analysis completed successfully")
        return JSONResponse(content=result)
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))
