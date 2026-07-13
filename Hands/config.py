'''
Este archivo trae la configuración del proyecto
'''

"""
Configuración global del proyecto HandConnect
"""

# Colores neón en formato BGR (OpenCV usa BGR)
NEON_COLORS = {
    'pink': (255, 0, 255),
    'cyan': (255, 255, 0),
    'green': (0, 255, 128),
    'yellow': (0, 255, 255),
    'purple': (180, 0, 255),
    'orange': (0, 165, 255),
    'red': (0, 0, 255),
    'blue': (255, 0, 0),
    'white': (255, 255, 255),
}

# Paleta de colores para el efecto arcoíris
RAINBOW_PALETTE = [
    (0, 0, 255),      # Rojo
    (0, 128, 255),    # Naranja
    (0, 255, 255),    # Amarillo
    (0, 255, 0),      # Verde
    (255, 255, 0),    # Cyan
    (255, 0, 255),    # Azul
    (255, 0, 128),    # Magenta
]

# Conexiones entre landmarks de la mano (MediaPipe)
HAND_CONNECTIONS = [
    # Pulgar
    (0, 1), (1, 2), (2, 3), (3, 4),
    # Índice
    (0, 5), (5, 6), (6, 7), (7, 8),
    # Medio
    (5, 9), (9, 10), (10, 11), (11, 12),
    # Anular
    (9, 13), (13, 14), (14, 15), (15, 16),
    # Meñique
    (13, 17), (17, 18), (18, 19), (19, 20),
    # Palma
    (0, 17),
]

# Configuración de MediaPipe
MEDIAPIPE_CONFIG = {
    'max_num_hands': 2,
    'model_complexity': 1,
    'min_detection_confidence': 0.7,
    'min_tracking_confidence': 0.5,
}

# Configuración de la cámara
CAMERA_CONFIG = {
    'width': 1280,
    'height': 720,
    'fps': 30,
    'camera_index': 0,
}

# Configuración de efectos
EFFECTS_CONFIG = {
    'line_thickness': 3,
    'glow_radius': 15,
    'particle_count': 20,
    'trail_length': 10,
}

# Modos de efecto disponibles
EFFECT_MODES = {
    1: 'neon_lines',      # Líneas neón entre manos
    2: 'rainbow',         # Arcoíris
    3: 'particles',       # Partículas
    4: 'laser',           # Efecto láser
    5: 'fire',            # Efecto fuego
}