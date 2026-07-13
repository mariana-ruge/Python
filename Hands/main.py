"""
HandConnect - Sistema de detección de manos con efectos neón
Archivo principal - VERSIÓN OPTIMIZADA
"""

import cv2
import numpy as np
import sys
import os
from hand_detector import HandDetector
from effects import NeonEffects
from gestures import GestureDetector
from config import CAMERA_CONFIG, EFFECT_MODES, NEON_COLORS

# Suprimir warnings de MediaPipe
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


def draw_rounded_rectangle(img, pt1, pt2, color, thickness=1, radius=15, fill_color=None):
    """
    Dibuja un rectángulo con esquinas redondeadas.
    Si fill_color no es None, rellena el rectángulo con ese color.
    """
    x1, y1 = pt1
    x2, y2 = pt2
    
    # Asegurar que las coordenadas estén en orden correcto
    if x1 > x2: x1, x2 = x2, x1
    if y1 > y2: y1, y2 = y2, y1
    
    # Si hay color de relleno, dibujar el rectángulo relleno
    if fill_color is not None:
        # Crear una máscara para el rectángulo redondeado
        overlay = img.copy()
        
        # Rectángulo central
        cv2.rectangle(overlay, (x1 + radius, y1), (x2 - radius, y2), fill_color, -1)
        # Rectángulos laterales
        cv2.rectangle(overlay, (x1, y1 + radius), (x2, y2 - radius), fill_color, -1)
        # Esquinas circulares
        cv2.circle(overlay, (x1 + radius, y1 + radius), radius, fill_color, -1)
        cv2.circle(overlay, (x2 - radius, y1 + radius), radius, fill_color, -1)
        cv2.circle(overlay, (x1 + radius, y2 - radius), radius, fill_color, -1)
        cv2.circle(overlay, (x2 - radius, y2 - radius), radius, fill_color, -1)
        
        # Mezclar con transparencia
        cv2.addWeighted(overlay, 0.85, img, 0.15, 0, img)
    
    # Dibujar el borde redondeado
    # Líneas rectas
    cv2.line(img, (x1 + radius, y1), (x2 - radius, y1), color, thickness, cv2.LINE_AA)
    cv2.line(img, (x1 + radius, y2), (x2 - radius, y2), color, thickness, cv2.LINE_AA)
    cv2.line(img, (x1, y1 + radius), (x1, y2 - radius), color, thickness, cv2.LINE_AA)
    cv2.line(img, (x2, y1 + radius), (x2, y2 - radius), color, thickness, cv2.LINE_AA)
    
    # Esquinas curvas
    cv2.ellipse(img, (x1 + radius, y1 + radius), (radius, radius), 180, 0, 90, color, thickness, cv2.LINE_AA)
    cv2.ellipse(img, (x2 - radius, y1 + radius), (radius, radius), 270, 0, 90, color, thickness, cv2.LINE_AA)
    cv2.ellipse(img, (x1 + radius, y2 - radius), (radius, radius), 90, 0, 90, color, thickness, cv2.LINE_AA)
    cv2.ellipse(img, (x2 - radius, y2 - radius), (radius, radius), 0, 0, 90, color, thickness, cv2.LINE_AA)


def draw_info_line(frame, x, y, label, value, font, label_color=(255, 255, 255), value_color=(255, 170, 0), scale=0.5):
    """
    Dibuja una línea de información con etiqueta en un color y valor en otro.
    Retorna la posición Y para la siguiente línea.
    """
    # Dibujar la etiqueta (variable) en blanco
    cv2.putText(frame, label, (x, y), font, scale, label_color, 1, cv2.LINE_AA)
    
    # Calcular posición del valor (después de la etiqueta)
    label_size, _ = cv2.getTextSize(label, font, scale, 1)
    value_x = x + label_size[0] + 8
    
    # Dibujar el valor en azul neón
    cv2.putText(frame, str(value), (value_x, y), font, scale, value_color, 1, cv2.LINE_AA)
    
    return y


class HandConnectApp:
    """Aplicación principal de HandConnect"""
    
    def __init__(self):
        # Inicializar componentes
        self.detector = HandDetector()
        self.effects = NeonEffects()
        self.gesture_detector = GestureDetector()
        
        # Configuración
        self.current_effect_mode = 1
        self.running = True
        self.fps = 0
        self.frame_count = 0
        self.fps_time = cv2.getTickCount()
        
        # Inicializar cámara
        self.cap = cv2.VideoCapture(CAMERA_CONFIG['camera_index'])
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAMERA_CONFIG['width'])
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAMERA_CONFIG['height'])
        self.cap.set(cv2.CAP_PROP_FPS, CAMERA_CONFIG['fps'])
        
        if not self.cap.isOpened():
            print("❌ Error: No se pudo abrir la cámara")
            sys.exit(1)
        
        print("✅ HandConnect iniciado correctamente")
        print(f"📷 Cámara: {CAMERA_CONFIG['width']}x{CAMERA_CONFIG['height']}")
        print("\n🎮 Controles:")
        print("   [Q/ESC] Salir")
        print("   [C] Limpiar efectos")
        print("   [S] Guardar screenshot")
        print("   [1-5] Cambiar modo de efecto")
        print("\n🎨 Modos de efecto:")
        for key, mode in EFFECT_MODES.items():
            print(f"   [{key}] {mode}")
    
    def run(self):
        """Loop principal de la aplicación"""
        while self.running:
            # Leer frame de la cámara
            ret, frame = self.cap.read()
            if not ret:
                print("❌ Error al leer el frame")
                break
            
            # Detectar manos
            frame, hands_data = self.detector.detect(frame)
            
            # Aplicar efectos
            frame = self.apply_effects(frame, hands_data)
            
            # Dibujar UI
            frame = self.draw_ui(frame, hands_data)
            
            # Mostrar frame
            cv2.imshow('HandConnect - Detección de Manos con Efectos Neón', frame)
            
            # Procesar teclas
            key = cv2.waitKey(1) & 0xFF
            self.handle_keypress(key, frame)
            
            # Calcular FPS
            self.calculate_fps()
        
        # Limpiar
        self.cleanup()
    
    def apply_effects(self, frame, hands_data):
            """Aplica los efectos visuales según el modo actual - VERSIÓN OPTIMIZADA"""
            img_height, img_width = frame.shape[:2]
            
            # Inicializar canvas de efectos
            self.effects._init_canvas(img_height, img_width)
            
            if len(hands_data) == 0:
                # Sin manos detectadas - actualizar partículas y chispas existentes
                self.effects.update_particles()
                self.effects.update_sparks()  # ✨ Actualizar chispas
                self.effects.apply_blur_to_canvas()
                frame = self.effects.composite_to_frame(frame)
                self.effects.update()
                return frame
            
            # Dibujar esqueleto de cada mano en el canvas
            for hand in hands_data:
                color = NEON_COLORS['cyan'] if hand['handedness'] == 'Right' else NEON_COLORS['pink']
                self.effects.draw_hand_skeleton(
                    hand['landmarks'], img_width, img_height, color
                )
            
            # Si hay dos manos, dibujar conexión entre ellas
            if len(hands_data) >= 2:
                effect_name = EFFECT_MODES[self.current_effect_mode]
                self.effects.draw_connection_between_hands(
                    hands_data[0]['landmarks'],
                    hands_data[1]['landmarks'],
                    img_width, img_height,
                    mode=effect_name
                )
            
            # Actualizar partículas
            self.effects.update_particles()
            
            # ✨ Actualizar chispas
            self.effects.update_sparks()
            
            # ⚡ Aplicar blur UNA sola vez a todo el canvas
            self.effects.apply_blur_to_canvas()
            
            # ⚡ Componer el canvas sobre el frame original
            frame = self.effects.composite_to_frame(frame)
            
            # Actualizar contador
            self.effects.update()
            
            return frame
    
    def draw_ui(self, frame, hands_data):
        """
        Dibuja la interfaz de usuario con recuadros mejorados:
        - Fondo gris oscuro
        - Bordes redondeados
        - Fuente tipo Helvetica (sans-serif)
        - Variables en blanco, valores en azul neón
        """
        img_height, img_width = frame.shape[:2]
        
        # Fuentes (Helvetica-like: FONT_HERSHEY_SIMPLEX es sans-serif limpia)
        font_title = cv2.FONT_HERSHEY_SIMPLEX
        font_normal = cv2.FONT_HERSHEY_SIMPLEX
        
        # Colores
        COLOR_BG = (40, 40, 40)          # Gris oscuro (BGR)
        COLOR_BORDER = (80, 80, 80)       # Borde gris medio
        COLOR_LABEL = (255, 255, 255)     # Blanco para variables
        COLOR_VALUE = (255, 170, 0)       # Azul neón para valores (cyan brillante)
        COLOR_TITLE = (255, 255, 255)     # Blanco para títulos
        
        # ============================================
        # RECUADRO 1: Información del sistema
        # ============================================
        box1_x1, box1_y1 = 15, 15
        box1_x2, box1_y2 = 320, 145
        box1_radius = 15
        
        # Dibujar recuadro redondeado con fondo gris oscuro
        draw_rounded_rectangle(
            frame, 
            (box1_x1, box1_y1), 
            (box1_x2, box1_y2),
            color=COLOR_BORDER,
            thickness=1,
            radius=box1_radius,
            fill_color=COLOR_BG
        )
        
        # Título del recuadro 1
        cv2.putText(frame, 'SYSTEM INFO', 
                   (box1_x1 + 20, box1_y1 + 30), 
                   font_title, 0.6, COLOR_TITLE, 1, cv2.LINE_AA)
        
        # Línea separadora sutil
        cv2.line(frame, 
                (box1_x1 + 15, box1_y1 + 40), 
                (box1_x2 - 15, box1_y1 + 40), 
                (70, 70, 70), 1, cv2.LINE_AA)
        
        # Líneas de información (variable en blanco, valor en azul neón)
        text_x = box1_x1 + 20
        y_cursor = box1_y1 + 65
        line_spacing = 25
        
        draw_info_line(frame, text_x, y_cursor, 
                      "Hands:", str(len(hands_data)), 
                      font_normal, COLOR_LABEL, COLOR_VALUE, 0.5)
        
        y_cursor += line_spacing
        draw_info_line(frame, text_x, y_cursor, 
                      "FPS:", f"{self.fps:.1f}", 
                      font_normal, COLOR_LABEL, COLOR_VALUE, 0.5)
        
        y_cursor += line_spacing
        draw_info_line(frame, text_x, y_cursor, 
                      "Mode:", EFFECT_MODES[self.current_effect_mode], 
                      font_normal, COLOR_LABEL, COLOR_VALUE, 0.5)
        
        # ============================================
        # RECUADRO 2: Gestos detectados
        # ============================================
        if hands_data:
            box2_x1, box2_y1 = 15, 160
            box2_height = 55 + (len(hands_data) * 28)
            box2_x2, box2_y2 = 320, 160 + box2_height
            box2_radius = 15
            
            # Dibujar recuadro redondeado
            draw_rounded_rectangle(
                frame, 
                (box2_x1, box2_y1), 
                (box2_x2, box2_y2),
                color=COLOR_BORDER,
                thickness=1,
                radius=box2_radius,
                fill_color=COLOR_BG
            )
            
            # Título del recuadro 2
            cv2.putText(frame, 'GESTURES', 
                       (box2_x1 + 20, box2_y1 + 30), 
                       font_title, 0.6, COLOR_TITLE, 1, cv2.LINE_AA)
            
            # Línea separadora
            cv2.line(frame, 
                    (box2_x1 + 15, box2_y1 + 40), 
                    (box2_x2 - 15, box2_y1 + 40), 
                    (70, 70, 70), 1, cv2.LINE_AA)
            
            # Información de gestos
            text_x = box2_x1 + 20
            y_cursor = box2_y1 + 65
            
            for i, hand in enumerate(hands_data):
                gesture = self.gesture_detector.detect_gesture(
                    hand['landmarks'], hand['handedness']
                )
                desc = self.gesture_detector.get_gesture_description(gesture)
                
                # Etiqueta: "Hand 1 (R):" en blanco
                label = f"Hand {i+1} ({hand['handedness'][0]}):"
                # Valor: descripción del gesto en azul neón
                value = desc
                
                draw_info_line(frame, text_x, y_cursor, 
                              label, value, 
                              font_normal, COLOR_LABEL, COLOR_VALUE, 0.5)
                
                y_cursor += 28
        
        # ============================================
        # Instrucciones inferiores (texto simple)
        # ============================================
        instructions_y = img_height - 20
        cv2.putText(frame, '[Q]uit   [C]lear   [S]ave   [1-5] Mode', 
                   (15, instructions_y), 
                   font_normal, 0.45, (150, 150, 150), 1, cv2.LINE_AA)
        
        return frame
    
    def calculate_fps(self):
        """Calcula los FPS actuales"""
        self.frame_count += 1
        current_time = cv2.getTickCount()
        elapsed = (current_time - self.fps_time) / cv2.getTickFrequency()
        
        if elapsed >= 1.0:
            self.fps = self.frame_count / elapsed
            self.frame_count = 0
            self.fps_time = current_time
    
    def handle_keypress(self, key, frame):
        """Maneja las pulsaciones de teclas"""
        if key == ord('q') or key == 27:  # 'q' o ESC
            self.running = False
        
        elif key == ord('c'):  # Limpiar
            self.effects.reset()
            print("🧹 Efectos limpiados")
        
        elif key == ord('s'):  # Screenshot
            filename = f'screenshot_{self.frame_count}.png'
            cv2.imwrite(filename, frame)
            print(f"📸 Screenshot guardado: {filename}")
        
        elif key in [ord(str(i)) for i in range(1, 6)]:  # Cambiar modo
            mode = int(chr(key))
            if mode in EFFECT_MODES:
                self.current_effect_mode = mode
                self.effects.reset()
                print(f"🎨 Modo cambiado a: {EFFECT_MODES[mode]}")
    
    def cleanup(self):
        """Limpia los recursos al salir"""
        print("\n👋 Cerrando HandConnect...")
        self.cap.release()
        if hasattr(self.detector, 'release'):
            self.detector.release()
        cv2.destroyAllWindows()
        print("✅ Recursos liberados correctamente")


if __name__ == '__main__':
    app = HandConnectApp()
    app.run()