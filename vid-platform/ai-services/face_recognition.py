import cv2
import numpy as np
import mediapipe as mp

class FaceRecognitionService:
    def __init__(self):
        self.mp_face_detection = mp.solutions.face_detection
        self.face_detection = self.mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5)

    def process_frame(self, frame_bytes):
        """
        Process an incoming camera frame for face detection.
        In a real scenario, this would compare embeddings against a MongoDB stored vector.
        """
        # Convert bytes to opencv image
        nparr = np.frombuffer(frame_bytes, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        # Convert to RGB for MediaPipe
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.face_detection.process(img_rgb)
        
        detections = []
        if results.detections:
            for detection in results.detections:
                bbox = detection.location_data.relative_bounding_box
                detections.append({
                    "score": detection.score[0],
                    "box": [bbox.xmin, bbox.ymin, bbox.width, bbox.height]
                })
        
        return detections

# Global AI Service Instance
ai_service = FaceRecognitionService()
