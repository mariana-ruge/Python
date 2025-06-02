#Importar librerias
import os
os.system('cls')
from turtle import *
import random

title('Estrella')

#Ajustar el color de fondo
bgcolor('black')

#Ajustar la velocidad del dibujo
speed(0)

#Declaramos el iniciador de la variable
x = 1

#Hacemos un ciclo para que se repita 400 veces hasta el dibujo
while x < 400:
    #Este movimiento genera los cuadrados al correr la graduacion de los pixeles
    forward(5+x)
    right(200)
    x+=1
    
    #Cambiar el color de forma aleatoria con el formato rgb
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0,255)
    
    #Establecer el modo del color
    colormode(255)
    #Cambiar el color del pincel
    pencolor(r,g,b)

mainloop()
