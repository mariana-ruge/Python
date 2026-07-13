'''
Reconoce los gestos con las manos
'''

"""
Módulo de detección de gestos con las manos
"""

import numpy as np


class GestureDetector:
    """Clase para detectar gestos de las manos"""
    
    def __init__(self):
        self.gesture_history = []
        self.current_gesture = 'none'
        
    def detect_gesture(self, landmarks, handedness='Right'):
        """
        Detecta el gesto actual basado en los landmarks
        Args:
            landmarks: Lista de 21 landmarks de la mano
            handedness: 'Left' o 'Right'
        Returns:
            str: Nombre del gesto detectado
        """
        if not landmarks or len(landmarks) < 21:
            return 'none'
        
        # Detectar qué dedos están levantados
        fingers_up = self._count_fingers_up(landmarks, handedness)
        
        # Detectar gestos
        gesture = 'none'
        
        # Puño cerrado (0 dedos levantados)
        if fingers_up == 0:
            gesture = 'fist'
        
        # Solo índice levantado
        elif fingers_up == 1 and self._is_finger_up(landmarks, 8):
            gesture = 'pointing'
        
        # Victoria (índice y medio)
        elif fingers_up == 2 and self._is_finger_up(landmarks, 8) and self._is_finger_up(landmarks, 12):
            gesture = 'victory'
        
        # Pulgar arriba
        elif fingers_up == 1 and self._is_finger_up(landmarks, 4):
            gesture = 'thumbs_up'
        
        # Pulgar abajo
        elif self._is_thumb_down(landmarks):
            gesture = 'thumbs_down'
        
        # Mano abierta (5 dedos)
        elif fingers_up >= 4:
            gesture = 'open_hand'
        
        # Pinza (pulgar e índice cerca)
        if self._is_pinch(landmarks):
            gesture = 'pinch'
        
        # Saludar (mano abierta moviéndose)
        if fingers_up >= 4 and self._is_waving(landmarks):
            gesture = 'waving'
        
        self.current_gesture = gesture
        self.gesture_history.append(gesture)
        if len(self.gesture_history) > 10:
            self.gesture_history.pop(0)
        
        return gesture
    
    def _count_fingers_up(self, landmarks, handedness):
        """Cuenta cuántos dedos están levantados"""
        count = 0
        
        # Pulgar (depende de la mano)
        if self._is_finger_up(landmarks, 4):
            count += 1
        
        # Otros dedos
        for tip_idx, pip_idx in [(8, 6), (12, 10), (16, 14), (20, 18)]:
            if self._is_finger_up(landmarks, tip_idx):
                count += 1
        
        return count
    
    def _is_finger_up(self, landmarks, tip_idx):
        """Verifica si un dedo está levantado comparando con su articulación"""
        if tip_idx == 4:  # Pulgar
            # Comparar x del pulgar con x del índice
            thumb_tip = landmarks[4]
            index_mcp = landmarks[5]
            # Para mano derecha, el pulgar está a la izquierda cuando está arriba
            return abs(thumb_tip['y'] - landmarks[3]['y']) > 0.05
        else:
            # Para otros dedos, comparar y del tip con y del pip
            tip = landmarks[tip_idx]
            pip = landmarks[tip_idx - 2]
            return tip['y'] < pip['y']
    
    def _is_thumb_down(self, landmarks):
        """Verifica si el pulgar está hacia abajo"""
        thumb_tip = landmarks[4]
        thumb_ip = landmarks[3]
        return thumb_tip['y'] > thumb_ip['y'] and thumb_tip['y'] > landmarks[0]['y']
    
    def _is_pinch(self, landmarks, threshold=0.05):
        """Verifica si hay gesto de pinza (pulgar e índice cerca)"""
        thumb_tip = landmarks[4]
        index_tip = landmarks[8]
        
        distance = np.sqrt(
            (thumb_tip['x'] - index_tip['x'])**2 + 
            (thumb_tip['y'] - index_tip['y'])**2
        )
        
        return distance < threshold
    
    def _is_waving(self, landmarks):
        """Detecta movimiento de saludo"""
        if len(self.gesture_history) < 5:
            return False
        
        # Verificar si la mano se ha movido horizontalmente
        wrist_x = [landmarks[0]['x']]
        return len(wrist_x) > 0
    
    def get_gesture_description(self, gesture):
        """Obtiene descripción del gesto"""
        descriptions = {
            'none': 'Sin gesto',
            'fist': '✊ Puño cerrado',
            'pointing': '☝️ Señalando',
            'victory': '✌️ Victoria',
            'thumbs_up': '👍 Pulgar arriba',
            'thumbs_down': ' Pulgar abajo',
            'open_hand': '🖐️ Mano abierta',
            'pinch': '🤏 Pinza',
            'waving': '👋 Saludo',
        }
        return descriptions.get(gesture, 'Desconocido')
    
    def get_gesture_color(self, gesture):
        """Obtiene color asociado al gesto (BGR)"""
        colors = {
            'none': (128, 128, 128),
            'fist': (0, 0, 255),        # Rojo
            'pointing': (255, 255, 0),   # Cyan
            'victory': (0, 255, 0),      # Verde
            'thumbs_up': (0, 255, 255),  # Amarillo
            'thumbs_down': (0, 0, 255),  # Rojo
            'open_hand': (255, 0, 255),  # Magenta
            'pinch': (180, 0, 255),      # Púrpura
            'waving': (0, 255, 128),     # Verde neón
        }
        return colors.get(gesture, (128, 128, 128))