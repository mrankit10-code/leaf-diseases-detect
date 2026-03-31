"""
Base64 Image Test for Leaf Disease Detection
===========================================

This script demonstrates how to send base64 image data directly to the detector.
"""

import json
import sys,os
import base64
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

# Add the Leaf Disease directory to Python path
sys.path.insert(0, str(Path(__file__).parent / "Leaf Disease"))

# Global detector instance (singleton pattern)
_detector_instance = None

try:
    from main import LeafDiseaseDetector
except ImportError as e:
    logger.error(f'Could not import LeafDiseaseDetector: {str(e)}')
    sys.exit(1)


def init_detector():
    """Initialize the detector on startup"""
    global _detector_instance
    if _detector_instance is None:
        logger.info("Initializing LeafDiseaseDetector...")
        _detector_instance = LeafDiseaseDetector()
        logger.info("✅ LeafDiseaseDetector ready")
    return _detector_instance


def get_detector():
    """Get or create the detector instance (lazy initialization)"""
    global _detector_instance
    if _detector_instance is None:
        init_detector()
    return _detector_instance


def test_with_base64_data(base64_image_string: str):
    """
    Test disease detection with base64 image data

    Args:
        base64_image_string (str): Base64 encoded image data
    """
    try:
        detector = get_detector()
        result = detector.analyze_leaf_image_base64(base64_image_string)
        logger.info("✅ Analysis successful")
        return result
    except Exception as e:
        logger.error(f'Analysis error: {str(e)}', exc_info=True)
        return None


def convert_image_to_base64_and_test(image_bytes: bytes):
    """
    Convert image bytes to base64 and test it

    Args:
        image_bytes (bytes): Image data in bytes
    """
    try:
        if not image_bytes:
            logger.error('No image bytes provided')
            return None

        base64_string = base64.b64encode(image_bytes).decode('utf-8')
        logger.info(f"Converted image to base64 ({len(base64_string)} characters)")
        return test_with_base64_data(base64_string)
    except Exception as e:
        logger.error(f'Base64 conversion error: {str(e)}', exc_info=True)
        return None


def main():
    """Test with base64 conversion"""
    image_path = "Media/brown-spot-4 (1).jpg"
    convert_image_to_base64_and_test(image_path)


if __name__ == "__main__":
    main()
