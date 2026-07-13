"""
Módulo de efectos visuales neón y partículas - VERSIÓN OPTIMIZADA
Líneas delgadas, manos verdes, degradé arcoíris entre manos, chispas salpicando
"""

import cv2
import numpy as np
from config import NEON_COLORS, RAINBOW_PALETTE, HAND_CONNECTIONS, EFFECTS_CONFIG


class NeonEffects:
    """Clase para generar efectos visuales sobre las manos"""
    
    def __init__(self):
        self.particles = []
        self.sparks = []  # ✨ Nuevo: sistema de chispas
        self.trail_points = []
        self.frame_count = 0
        self.effect_canvas = None
        self.sharp_canvas = None
        
    def _init_canvas(self, height, width):
        """Inicializa los canvas de efectos"""
        if (self.effect_canvas is None or 
            self.effect_canvas.shape[0] != height or 
            self.effect_canvas.shape[1] != width):
            self.effect_canvas = np.zeros((height, width, 3), dtype=np.uint8)
            self.sharp_canvas = np.zeros((height, width, 3), dtype=np.uint8)
    
    def draw_neon_line_fast(self, pt1, pt2, color, thickness=1):
        """Dibuja una línea delgada en el canvas de efectos"""
        # Glow sutil (línea gruesa que se difuminará)
        cv2.line(self.effect_canvas, pt1, pt2, color, thickness + 3, cv2.LINE_AA)
        # Línea central nítida y delgada
        cv2.line(self.sharp_canvas, pt1, pt2, color, thickness, cv2.LINE_AA)
        # Línea blanca muy fina en el centro para brillo
        cv2.line(self.sharp_canvas, pt1, pt2, (200, 200, 200), max(1, thickness - 1), cv2.LINE_AA)
    
    def draw_rainbow_gradient_line(self, pt1, pt2, thickness=1):
        """
        Dibuja una línea con degradé arcoíris entre dos puntos
        El color cambia gradualmente a lo largo de la línea
        """
        dx = pt2[0] - pt1[0]
        dy = pt2[1] - pt1[1]
        length = int(np.sqrt(dx**2 + dy**2))
        
        if length == 0:
            return
        
        # Dibujar segmentos con colores del arcoíris
        for i in range(length):
            t = i / length
            # Interpolar color del arcoíris
            color_idx = int(t * (len(RAINBOW_PALETTE) - 1))
            color = RAINBOW_PALETTE[color_idx]
            
            # Calcular punto actual
            x = int(pt1[0] + dx * t)
            y = int(pt1[1] + dy * t)
            
            # Punto siguiente para el segmento
            t_next = (i + 1) / length
            x_next = int(pt1[0] + dx * t_next)
            y_next = int(pt1[1] + dy * t_next)
            
            # Glow en canvas de efectos
            cv2.line(self.effect_canvas, (x, y), (x_next, y_next), color, thickness + 3, cv2.LINE_AA)
            # Línea nítida
            cv2.line(self.sharp_canvas, (x, y), (x_next, y_next), color, thickness, cv2.LINE_AA)
    
    def draw_neon_point_fast(self, x, y, color, radius=3):
        """Dibuja un punto delgado en el canvas de efectos"""
        cv2.circle(self.effect_canvas, (x, y), radius + 2, color, -1)
        cv2.circle(self.sharp_canvas, (x, y), radius, color, -1)
        cv2.circle(self.sharp_canvas, (x, y), max(1, radius - 1), (200, 200, 200), -1)
    
    def apply_blur_to_canvas(self):
        """Aplica blur al canvas de efectos UNA sola vez"""
        self.effect_canvas = cv2.GaussianBlur(self.effect_canvas, (11, 11), 0)
    
    def composite_to_frame(self, frame):
        """Compone los canvas sobre el frame original"""
        # Sumar glow + líneas nítidas
        result = cv2.add(frame, self.effect_canvas)
        result = cv2.add(result, self.sharp_canvas)
        # Limpiar ambos canvas
        self.effect_canvas.fill(0)
        self.sharp_canvas.fill(0)
        return result
    
    def draw_hand_skeleton(self, landmarks, img_width, img_height, color=None):
        """
        Dibuja el esqueleto de la mano con líneas DELGADAS y color VERDE
        También genera chispas desde las puntas de los dedos
        """
        # Color por defecto: VERDE NEÓN
        if color is None:
            color = (0, 255, 100)  # Verde neón brillante (BGR)
        
        # Dibujar conexiones con líneas delgadas
        for connection in HAND_CONNECTIONS:
            start_idx, end_idx = connection
            if start_idx < len(landmarks) and end_idx < len(landmarks):
                pt1 = (int(landmarks[start_idx]['x'] * img_width), 
                       int(landmarks[start_idx]['y'] * img_height))
                pt2 = (int(landmarks[end_idx]['x'] * img_width), 
                       int(landmarks[end_idx]['y'] * img_height))
                
                self.draw_neon_line_fast(pt1, pt2, color, thickness=1)
        
        # Dibujar puntos (landmarks) pequeños
        for i, landmark in enumerate(landmarks):
            x = int(landmark['x'] * img_width)
            y = int(landmark['y'] * img_height)
            self.draw_neon_point_fast(x, y, color, radius=3)
        
        # ✨ Generar chispas desde las puntas de los dedos
        finger_tips = [4, 8, 12, 16, 20]  # Pulgar, índice, medio, anular, meñique
        for tip_idx in finger_tips:
            if tip_idx < len(landmarks):
                x = int(landmarks[tip_idx]['x'] * img_width)
                y = int(landmarks[tip_idx]['y'] * img_height)
                self._generate_sparks(x, y, intensity=0.3)  # 30% de probabilidad por frame
    
    def _generate_sparks(self, x, y, intensity=0.5):
        """
        Genera chispas que salpican desde un punto
        Args:
            x, y: Posición de origen
            intensity: Probabilidad de generar chispas (0.0 a 1.0)
        """
        if np.random.random() > intensity:
            return
        
        # Número de chispas a generar (2-5)
        num_sparks = np.random.randint(2, 6)
        
        for _ in range(num_sparks):
            # Velocidad inicial aleatoria (dirección y magnitud)
            angle = np.random.uniform(0, 2 * np.pi)
            speed = np.random.uniform(2, 8)
            
            vx = np.cos(angle) * speed
            vy = np.sin(angle) * speed - 2  # Ligera tendencia hacia arriba
            
            # Color de la chispa (blanco brillante → amarillo → naranja)
            life = np.random.randint(15, 30)
            if life > 20:
                color = (200, 220, 255)  # Blanco azulado brillante
            elif life > 10:
                color = (100, 200, 255)  # Amarillo brillante
            else:
                color = (50, 150, 255)   # Naranja
            
            self.sparks.append({
                'x': x,
                'y': y,
                'vx': vx,
                'vy': vy,
                'life': life,
                'max_life': life,
                'color': color,
                'size': np.random.randint(1, 3)
            })
    
    def update_sparks(self):
        """
        Actualiza y dibuja las chispas con física simple
        Las chispas tienen velocidad, gravedad y se desvanecen
        """
        new_sparks = []
        
        for spark in self.sparks:
            # Actualizar posición con velocidad
            spark['x'] += spark['vx']
            spark['y'] += spark['vy']
            
            # Aplicar gravedad ligera
            spark['vy'] += 0.3
            
            # Aplicar fricción
            spark['vx'] *= 0.95
            spark['vy'] *= 0.95
            
            # Reducir vida
            spark['life'] -= 1
            
            if spark['life'] > 0:
                # Calcular alpha basado en vida restante
                alpha = spark['life'] / spark['max_life']
                
                # Cambiar color mientras envejece (blanco → amarillo → naranja → rojo)
                if alpha > 0.7:
                    color = (200, 220, 255)  # Blanco brillante
                elif alpha > 0.4:
                    color = (100, 200, 255)  # Amarillo
                elif alpha > 0.2:
                    color = (50, 150, 255)   # Naranja
                else:
                    color = (30, 80, 200)    # Rojo oscuro
                
                # Aplicar alpha al color
                color = tuple(int(c * alpha) for c in color)
                
                # Dibujar chispa en canvas de efectos (con glow)
                cv2.circle(self.effect_canvas, (int(spark['x']), int(spark['y'])), 
                          spark['size'] + 2, color, -1)
                # Dibujar núcleo brillante en canvas nítido
                cv2.circle(self.sharp_canvas, (int(spark['x']), int(spark['y'])), 
                          spark['size'], (255, 255, 255), -1)
                
                new_sparks.append(spark)
        
        self.sparks = new_sparks
    
    def draw_connection_between_hands(self, hand1_landmarks, hand2_landmarks, 
                                       img_width, img_height, mode='rainbow'):
        """
        Dibuja conexiones entre dos manos con DEGRADÉ ARCOÍRIS
        También genera chispas en los puntos de conexión
        """
        # Conectar centros de las palmas con degradé arcoíris
        palm1 = self._get_palm_center(hand1_landmarks)
        palm2 = self._get_palm_center(hand2_landmarks)
        
        if palm1 and palm2:
            pt1 = (int(palm1['x'] * img_width), int(palm1['y'] * img_height))
            pt2 = (int(palm2['x'] * img_width), int(palm2['y'] * img_height))
            
            if mode == 'fire':
                self._draw_fire_effect(pt1, pt2)
            else:
                # SIEMPRE degradé arcoíris (modo por defecto)
                self.draw_rainbow_gradient_line(pt1, pt2, thickness=1)
                # ✨ Generar chispas en el punto medio
                mid_x = (pt1[0] + pt2[0]) // 2
                mid_y = (pt1[1] + pt2[1]) // 2
                self._generate_sparks(mid_x, mid_y, intensity=0.2)
        
        # Conectar dedos correspondientes con degradé arcoíris
        finger_pairs = [(4, 4), (8, 8), (12, 12), (16, 16), (20, 20)]
        
        for idx, (finger1, finger2) in enumerate(finger_pairs):
            if finger1 < len(hand1_landmarks) and finger2 < len(hand2_landmarks):
                pt1 = (int(hand1_landmarks[finger1]['x'] * img_width), 
                       int(hand1_landmarks[finger1]['y'] * img_height))
                pt2 = (int(hand2_landmarks[finger2]['x'] * img_width), 
                       int(hand2_landmarks[finger2]['y'] * img_height))
                
                if mode == 'particles':
                    color = RAINBOW_PALETTE[idx % len(RAINBOW_PALETTE)]
                    self._add_particles(pt1, pt2, color)
                else:
                    # Degradé arcoíris para cada dedo
                    self.draw_rainbow_gradient_line(pt1, pt2, thickness=1)
                    # ✨ Generar chispas en los puntos de conexión
                    self._generate_sparks(pt1[0], pt1[1], intensity=0.15)
                    self._generate_sparks(pt2[0], pt2[1], intensity=0.15)
    
    def _draw_fire_effect(self, pt1, pt2):
        """Efecto de fuego entre manos"""
        dx = pt2[0] - pt1[0]
        dy = pt2[1] - pt1[1]
        steps = int(np.sqrt(dx**2 + dy**2) / 5)
        
        for i in range(steps):
            t = i / max(steps, 1)
            x = int(pt1[0] + dx * t + np.random.randint(-10, 10))
            y = int(pt1[1] + dy * t + np.random.randint(-10, 10))
            
            color = RAINBOW_PALETTE[np.random.randint(0, 3)]
            radius = np.random.randint(2, 5)
            cv2.circle(self.effect_canvas, (x, y), radius, color, -1)
    
    def _add_particles(self, pt1, pt2, color):
        """Agregar partículas a lo largo de la línea"""
        dx = pt2[0] - pt1[0]
        dy = pt2[1] - pt1[1]
        
        for _ in range(EFFECTS_CONFIG['particle_count']):
            t = np.random.random()
            x = int(pt1[0] + dx * t + np.random.randint(-20, 20))
            y = int(pt1[1] + dy * t + np.random.randint(-20, 20))
            
            self.particles.append({
                'x': x,
                'y': y,
                'color': color,
                'life': 30,
                'size': np.random.randint(1, 4)
            })
    
    def update_particles(self):
        """Actualizar partículas (dibuja en el canvas)"""
        new_particles = []
        
        for particle in self.particles:
            particle['life'] -= 1
            particle['y'] -= 2
            particle['x'] += np.random.randint(-2, 3)
            
            if particle['life'] > 0:
                alpha = particle['life'] / 30
                color = tuple(int(c * alpha) for c in particle['color'])
                cv2.circle(self.effect_canvas, (particle['x'], particle['y']), 
                          particle['size'], color, -1)
                new_particles.append(particle)
        
        self.particles = new_particles
    
    def update(self):
        """Actualizar frame count"""
        self.frame_count += 1
    
    def reset(self):
        """Resetear efectos"""
        self.particles = []
        self.sparks = []  # ✨ Limpiar chispas
        self.trail_points = []
        self.frame_count = 0
        if self.effect_canvas is not None:
            self.effect_canvas.fill(0)
        if self.sharp_canvas is not None:
            self.sharp_canvas.fill(0)
    
    def _get_palm_center(self, landmarks):
        """Obtener centro de la palma"""
        palm_indices = [0, 5, 9, 13, 17]
        x = sum(landmarks[i]['x'] for i in palm_indices) / 5
        y = sum(landmarks[i]['y'] for i in palm_indices) / 5
        return {'x': x, 'y': y}