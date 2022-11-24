import os
import random
import fruteria as f
os.system('cls')

#triqui para jugar entre 2
'''
    [
          1    2    3 
       A ['X', 'O', 'X']
       B ['O', 'X', ' ']
       C ['X', ' ', 'O']
    ]

    -Registrar jugadores
    -Asignar turno
    -Pintar tablero
    -Hacer jugada
    -Verificar ganador

'''
filas = {"A": 0, "B": 1, "C": 2}
tablero = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

def asignar_turno(lista_jugadores):
    jugador_inicia = random.choice(lista_jugadores)
    return jugador_inicia

def pintar_tablero():
    for fila in tablero:
        imprimible = ""
        for item in fila:
            imprimible += ("|"+(" _ " if item == " " else item )+ "|")
        print(imprimible.replace("||", "|"))


def pedir_jugada(letra):
    cuadro = list(input("¿Cuál casilla quieres marcar? : ").upper())
    if len(cuadro) != 2     or cuadro[0] not in filas.keys() or cuadro [1] not in "123":
        f.clear_screen()
        pintar_tablero()
        print("Casilla no válida")
        pedir_jugada()
    else:
        fila = filas.get(cuadro[0])
        columna = int(cuadro[1])-1
        if esta_ocupado(fila, columna):
            print("Casilla Ocupada")
            pedir_jugada()
        else:
            tablero[fila][columna] = letra
    

def esta_ocupado(fila, columna):
    contenido = tablero[fila][columna]
    return True if contenido != " " else False



def jugar(jugador_1, jugador_2):
    for numero_jugada in range(9):
        f.clear_screen()
        if numero_jugada % 2 == 0:
            letra = "X"
            nombre = jugador_1
        else:
            letra = "O"
            nombre = jugador_2
        print("Turno de", nombre, "jugará con ", letra)
        pintar_tablero()
        pedir_jugada(letra)


def hay_triqui():
    #Buscar como cambiar el marcador
    pass           


def run():
    f.clear_screen()
    lista_jugadores = [input(" Jugador "+str(i+1)+":") for i in range(2)]
    jugador_1 = asignar_turno(lista_jugadores)
    jugador_2 = lista_jugadores[1]
    print("Inicia", asignar_turno(lista_jugadores), "Con las X")
    jugar(jugador_1, jugador_2)
    hay_triqui()



if __name__ == "__main__":
    run()