import os
os.system('cls')

#Importar librerias
import turtle

#Crear el objeto turtle
t = turtle.Turtle()
#Crear el objeto para la pantalla
s = turtle.Screen()
#Establecer el color de fondo como nego
s.bgcolor('black')

#Ponerle un color al lapiz
t.pencolor('white')

#iniciador
a = 0
b = 0 

#Ajustar la velocidad
t.speed(0)

#Levantar el lapiz para mover la posicion
t.penup()

#Mover la posicion del lapiz
t.goto(0, 200)

#Bajar el lapiz
t.pendown()

#Crear el ciclo para hacer el dibujo
while True:
    #Movemos cierta cantidad de pixeles adelante y a la derecha
    t.forward(a)
    t.right(b)
    #Incrementar las variables
    a+= 3
    b += 1
    #Romper para evitar caer en un bucle infinito
    if b == 210:
        break
    
    #Esconder el cursor
    t.hideturtle



#Llamar al dibujo ya listo
turtle.done()