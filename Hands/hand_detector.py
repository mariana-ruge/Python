"""
Módulo de detección de manos usando MediaPipe Tasks Python API
Compatible con Python 3.14 y MediaPipe 0.10.35
"""

import cv2
import numpy as np
import os
import mediapipe as mp
from mediapipe.tasks.python import BaseOptions, vision
from config import MEDIAPIPE_CONFIG


class HandDetector:
    """Clase para detectar y rastrear manos en tiempo real"""
    
    def __init__(self):
        # Ruta al modelo
        model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "hand_landmarker.task")
        
        if not os.path.exists(model_path):
            raise FileNotFoundError(
                f"❌ No se encontró el modelo en: {model_path}\n"
                "Descárgalo con:\n"
                "Invoke-WebRequest -Uri 'https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task' -OutFile 'hand_landmarker.task'"
            )
        
        print(f"📦 Cargando modelo desde: {model_path}")
        
        # Acceder a las clases desde el módulo vision
        HandLandmarker = vision.HandLandmarker
        HandLandmarkerOptions = vision.HandLandmarkerOptions
        
        # RunningMode
        try:
            RunningMode = vision.RunningMode
            running_mode = RunningMode.VIDEO
            print("✅ RunningMode encontrado en vision")
        except AttributeError:
            running_mode = 2
            print("⚠️ Usando valor numérico para RunningMode.VIDEO (2)")
        
        # Configurar opciones
        options = HandLandmarkerOptions(
            base_options=BaseOptions(model_asset_path=model_path),
            running_mode=running_mode,
            num_hands=MEDIAPIPE_CONFIG['max_num_hands'],
            min_hand_detection_confidence=MEDIAPIPE_CONFIG['min_detection_confidence'],
            min_tracking_confidence=MEDIAPIPE_CONFIG['min_tracking_confidence'],
            min_hand_presence_confidence=0.5
        )
        
        # Crear el detector
        self.hand_landmarker = HandLandmarker.create_from_options(options)
        
        # Almacenar resultados
        self.hands_data = []
        self.landmarks_list = []
        self.last_timestamp_ms = 0
        
        print("✅ MediaPipe Tasks Python API configurado correctamente")
        
    def detect(self, frame):
        """Detecta las manos en el frame"""
        # Convertir BGR a RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Crear objeto MPImage
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
        
        # Timestamp incremental
        self.last_timestamp_ms += 33
        
        # Detectar
        detection_result = self.hand_landmarker.detect_for_video(
            mp_image, 
            self.last_timestamp_ms
        )
        
        self.hands_data = []
        self.landmarks_list = []
        
        if detection_result.hand_landmarks:
            for hand_idx, hand_landmarks in enumerate(detection_result.hand_landmarks):
                landmarks = []
                for landmark in hand_landmarks:
                    landmarks.append({
                        'x': landmark.x,
                        'y': landmark.y,
                        'z': landmark.z
                    })
                
                # Lateralidad
                if detection_result.handedness and len(detection_result.handedness) > hand_idx:
                    handedness = detection_result.handedness[hand_idx][0].category_name
                else:
                    handedness = 'Right'
                
                # Bounding box
                landmark_array = np.array([(l['x'], l['y']) for l in landmarks])
                x_min = int(np.min(landmark_array[:, 0]) * frame.shape[1])
                y_min = int(np.min(landmark_array[:, 1]) * frame.shape[0])
                x_max = int(np.max(landmark_array[:, 0]) * frame.shape[1])
                y_max = int(np.max(landmark_array[:, 1]) * frame.shape[0])
                
                center_x = int((x_min + x_max) / 2)
                center_y = int((y_min + y_max) / 2)
                
                hand_data = {
                    'id': hand_idx,
                    'landmarks': landmarks,
                    'handedness': handedness,
                    'bbox': (x_min, y_min, x_max, y_max),
                    'center': (center_x, center_y),
                }
                
                self.hands_data.append(hand_data)
                self.landmarks_list.append(landmarks)
        
        return frame, self.hands_data
    
    def get_finger_positions(self, landmarks):
        """Obtiene las posiciones de las puntas de los dedos"""
        if not landmarks:
            return None
        
        finger_tips = {
            'thumb': landmarks[4],
            'index': landmarks[8],
            'middle': landmarks[12],
            'ring': landmarks[16],
            'pinky': landmarks[20]
        }
        
        return finger_tips
    
    def get_palm_center(self, landmarks):
        """Obtiene el centro de la palma"""
        if not landmarks:
            return None
        
        palm_landmarks = [0, 5, 9, 13, 17]
        x = sum(landmarks[i]['x'] for i in palm_landmarks) / 5
        y = sum(landmarks[i]['y'] for i in palm_landmarks) / 5
        
        return {'x': x, 'y': y}
    
    def release(self):
        """Liberar recursos"""
        if hasattr(self, 'hand_landmarker'):
            self.hand_landmarker.close()