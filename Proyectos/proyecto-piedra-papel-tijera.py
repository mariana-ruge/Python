#Limpiando la consola
import os
os.system('cls')
import random


#Creando variables
print("Vamos a jugar Piedra, Papel, o Tijera, a continuación escoge una opción: ")

rondas = 1
puntos_usuario = 0
puntos_computadora = 0
print('*' * 10)
print("RONDA 1")
print('*' * 10)

while True:
    opcion_usuario = input("Piedra, Papel, o Tijera :   ")
    opcion_usuario = opcion_usuario.capitalize()
    opciones = ('Piedra', 'Papel', 'Tijera') #Las opciones son una tupla
    opcion_computadora = random.choice(opciones)

    print("Opcion del usuario ->", opcion_usuario)
    print("Opción de la computadora ->",opcion_computadora)

    if not opcion_usuario in opciones:
        print("Opcion no válida")
        continue

    #Creando juego
    if opcion_usuario ==  opcion_computadora:
        print("Empate")
    elif opcion_usuario == 'Piedra':
        if opcion_computadora == 'Tijera':
            print('Piedra gana a tijera')
            print('Gana el usuario')
            puntos_usuario += 1
        else:
            print("Papel gana a piedra")
            print("Gana la computadora")
            puntos_computadora +=1
    elif opcion_usuario == 'Papel':
        if opcion_computadora == 'Piedra':
            print("Papel cubre a la piedra")
            print("Gana el usuario")
            puntos_usuario +=1
        else:
            print("La tijera corta el papel")
            print("Gana la computadora")
            puntos_computadora += 1
    elif opcion_usuario == 'Tijera':
        if opcion_computadora == 'Papel':
            print("Tijera gana a papel")
            print("Gana el usuario")
            puntos_usuario += 1
        else:
            print("Piedra gana a tijera")
            print("Gana la computadora")
            puntos_computadora += 1
    else:
        print("Error")

    if puntos_usuario == 3:
        print('Gana el usuario')
        break
    if puntos_computadora == 3:
        print('Gana la computadora')
    rondas += 1