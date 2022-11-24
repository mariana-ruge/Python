import os
os.system('cls')
import random

'''
    si el item es un numero sumar
    sino sera una lista, calcular la suma de una lista...

'''

def suma_lista(lista):
    sumatoria = 0
    for elemento in lista:
        if type(elemento) is list:
            sumatoria += suma_lista(elemento)
        else:
            sumatoria += elemento
    return sumatoria
        


def sumar_elementos(lista_2):
    sumatoria = 0
    if len(len(lista_2)==1):
        sumatoria == lista_2[0]
    else:
        sumatoria = lista[0] + sumar_elementos(lista[1:])
    return sumatoria


def adivinar(numero_secreto):
    numero = int(input("escriba: "))
    if numero == numero_secreto:
        print("felicitaciones")
    else:
        adivinar(numero_secreto) 
    



if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5]
    numero_secreto=random.choice(lista)
    print(numero_secreto)
    adivinar(numero_secreto)