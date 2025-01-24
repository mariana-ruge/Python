import os
os.system('cls')
import turtle as tur

# Configuración inicial
tur.setup(700, 700)
tur.speed(0)
tur.tracer(10)
tur.width(2)
tur.bgcolor("black")
tur.color("white")

# Posicionar la tortuga en el centro inferior
tur.penup()
tur.setpos(0, -250)
tur.pendown()

tur.left(90)
tur.speed(150)

# Definición de la función recursiva para dibujar el árbol
def tree(i):
    if i < 10:  # Caso base
        return
    else:
        tur.forward(i)  # Dibuja una línea recta
        tur.left(30)  # Gira 30 grados hacia la izquierda
        tree(4 * i / 5)  # Rama izquierda (reducida al 80%)
        tur.right(60)  # Gira 60 grados hacia la derecha
        tree(4 * i / 5)  # Rama derecha (reducida al 80%)
        tur.left(30)  # Regresa a la orientación original
        tur.backward(i)  # Retrocede para volver a la posición inicial

# Llama a la función para dibujar el árbol
tree(100)

# Finaliza el dibujo
tur.done()
