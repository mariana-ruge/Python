#Limpiando la consola
import os
os.system('cls')
import random


#Creando variables
print("Vamos a jugar Piedra, Papel, o Tijera, a continuación escoge una opción: ")
puntos_usuario = 0
puntos_computadora = 0

#Función para obtener las opciones
def escoger_opcion():
    opcion_usuario = input("Piedra, Papel, o Tijera :   ")
    opcion_usuario = opcion_usuario.capitalize()
    opciones = ('Piedra', 'Papel', 'Tijera') #Las opciones son una tupla
    

    if not opcion_usuario in opciones:
        print("Opcion no válida")
        return None, None

    opcion_computadora = random.choice(opciones)

    print("Opcion del usuario ->", opcion_usuario)
    print("Opción de la computadora ->",opcion_computadora)

    

    return opcion_usuario, opcion_computadora
        


def definir_reglas(opcion_usuario, opcion_computadora, puntos_usuario, puntos_computadora):
    #Creando juego
    if opcion_usuario ==  opcion_computadora:
        print("Empate")
        return 0
    elif opcion_usuario == 'Piedra':
        if opcion_computadora == 'Tijera':
            print('Piedra gana a tijera')
            print('Gana el usuario')
            return 1
        else:
            print("Papel gana a piedra")
            print("Gana la computadora")
            return -1
        
    elif opcion_usuario == 'Papel':
        if opcion_computadora == 'Piedra':
            print("Papel cubre a la piedra")
            print("Gana el usuario")
            return 1
        else:
            print("La tijera corta el papel")
            print("Gana la computadora")
            return -1
    elif opcion_usuario == 'Tijera':
        if opcion_computadora == 'Papel':
            print("Tijera gana a papel")
            print("Gana el usuario")
            return 1
        else:
            print("Piedra gana a tijera")
            print("Gana la computadora")
            return -1
    else:
        print("Error")
        return 0





def definir_ganador(puntos_computadora, puntos_usuario):
    if puntos_usuario == 3:
            print(puntos_usuario)
            print('Gana el usuario')
    elif puntos_computadora == 3:
            print(puntos_computadora)
            print('Gana la computadora')


def correr_juego():
    puntos_usuario = 0
    puntos_computadora = 0
    rondas = 1
    while puntos_usuario < 3 and puntos_computadora < 3:
        print('*' * 10)
        print("RONDA", rondas)
        print('*' * 10)

        print("**MARCADOR**")
        print("Puntos usuario", puntos_usuario)
        print("Puntos computadora", puntos_computadora)

        opcion_usuario, opcion_computadora = escoger_opcion()
    
        print("**Desarrollo del Juego**")
        resultado = definir_reglas(opcion_usuario, opcion_computadora, puntos_usuario, puntos_computadora)
        if resultado == 1: 
            puntos_usuario +=1
        elif resultado == -1:
            puntos_computadora +=1
        definir_ganador(puntos_computadora, puntos_usuario)
        rondas += 1

        
correr_juego();

