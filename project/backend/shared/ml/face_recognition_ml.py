"""
ML Face Recognition Service
Uses face_recognition (dlib) + OpenCV for enrollment and verification
"""
import io
import numpy as np
from typing import Optional
from loguru import logger

try:
    import face_recognition
    FACE_RECOGNITION_AVAILABLE = True
except ImportError:
    FACE_RECOGNITION_AVAILABLE = False
    logger.warning("face_recognition not available — using stub")

try:
    import cv2
    CV2_AVAILABLE = True
except ImportError:
    CV2_AVAILABLE = False


class FaceRecognitionService:
    def __init__(self, tolerance: float = 0.6):
        self.tolerance = tolerance
        self.model = "hog"  # "cnn" for GPU

    def encode_face(self, image_bytes: bytes) -> Optional[np.ndarray]:
        """Encode face from image bytes → numpy array"""
        if not FACE_RECOGNITION_AVAILABLE:
            return np.random.rand(128)  # stub for development

        try:
            img_array = np.frombuffer(image_bytes, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            encodings = face_recognition.face_encodings(
                rgb_img,
                face_recognition.face_locations(rgb_img, model=self.model)
            )

            if not encodings:
                return None
            return encodings[0]

        except Exception as e:
            logger.error(f"Face encoding error: {e}")
            return None

    def compare_faces(self, stored_image_bytes: bytes, new_image_bytes: bytes) -> Optional[float]:
        """
        Compare two face images.
        Returns face distance (lower = more similar, < 0.6 is a match)
        """
        if not FACE_RECOGNITION_AVAILABLE:
            return np.random.uniform(0.3, 0.7)  # stub

        try:
            enc1 = self.encode_face(stored_image_bytes)
            enc2 = self.encode_face(new_image_bytes)

            if enc1 is None or enc2 is None:
                return None

            distances = face_recognition.face_distance([enc1], enc2)
            return float(distances[0])

        except Exception as e:
            logger.error(f"Face comparison error: {e}")
            return None

    def detect_faces_count(self, image_bytes: bytes) -> int:
        """Detect number of faces in image (for kiosk anti-spoofing)"""
        if not FACE_RECOGNITION_AVAILABLE:
            return 1

        try:
            img_array = np.frombuffer(image_bytes, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            locations = face_recognition.face_locations(rgb_img, model=self.model)
            return len(locations)
        except Exception as e:
            logger.error(f"Face detection error: {e}")
            return 0
