from cmath import sqrt
import os
import math
from re import A
from unicodedata import name
os.system('cls')

#ejercicios varios

# 1. Escribir un programa que calcule el área de un paraboloide dados r y h e imprima la solución
    #Fórmula: A = 3.6r*math.isqrt(r**2 + 4/3(h**2) )
def area():
    r = float(input())
    h = float(input())
    a = (3.6 * r)
    b = (r**2 + 4/3*(h**2))
    c = math.sqrt(b)
    d = a * c
    print(d)

#2. Se ingresan 4 valores, cada par corresponde al peso y edad de un individuo, se quiere ordenar estas 2 
    #personas bajo el siguiente criterio: se debe indicar el de mayor peso, si los dos tienen el mismo peso
    #se debe indicar el de menor edad, si los dos individuos tienen el mismo peso y edad se debe indicar iguales
'''
 a = ['1', '2', '3', '4']
    print([int(x) for x in a])
'''
def ordenamiento():
    individuos = input().split()
    #Convertir una lista a enteros con un ciclo
    convertir = ([int(x) for x in individuos])
    print(convertir)
    #Sacando los indices de las personas
    persona_uno = [convertir[0], convertir[1]]
    persona_dos = [convertir[2], convertir[3]]

    #Ordenar a las personas
    if convertir[0] > convertir[2]:
        print(persona_uno)
        print("Primero")
    elif convertir[0] < convertir[2]:
        print(persona_dos)
        print("Segundo")
    elif convertir[1] < convertir[3]:
        print(persona_uno)
        print("Primero")
    elif convertir[1] > convertir[3]:
        print(persona_dos)
        print("Segundo")
    else:
            print("Las personas son iguales")

#3 Formula: Reciba como entrada tres números x, y, z con z != 0 y calcule la fórmula
#(x^2 + y^2)/z

def formula():
    x, y, z = input().split()
    x = float(x)
    y = float(y)
    z = float(z)
    
    if z == 0:
        print("Error")
    else:
        opercion = (x**2 + y**2) /z
        decimal = float(opercion) 
        print(decimal)

#4 Escriba un programa que reciba como entrada un entero n e imprima
#la suma de sus digitos.
def suma_digitos():
    numero = list(input())
    transformar = ([int(x) for x in numero])
    resultado = sum(transformar)
    print(resultado)

#5 Cuadrado
#   Diseñe un cuadrado en Python exacto
def  cuadrado():
    largo_lados = int(input())
    altura_lados = int(input())

    for i in range(largo_lados):
        print(" * ", end="")
    print()

    for i in range(altura_lados - 2):
        print(" * ", end=" ")
        for j in range(largo_lados - 2):
            print("  ", end=" ")
        print("*")

    for i in range(largo_lados):
        print(" * ", end="")


#6 Triángulo
# Dibujar un triángulo con Python

def triangulo():
    numero = int(input("Introduce el número de veces "))
    for i in range(numero + 1):
        print("*" * i)
    #Triangulo invertido
    for i in range(numero+1):
        espacios = numero - i
        print(' '* espacios + '*' * i)
    #Triangulo centrado
    for i in range(numero + 1):
        espacios = numero - i
        print(' '*espacios+'* ' * i)

#Dibujar una ventana

def ventana():
    largo = int(input())
    altura = int(input())

    for i in range(largo):
        print("  * ", end="")
    print()

    for i in range(altura):
        print(" ", end=" * ")
        for i in range(largo):
            print(" ", end=" ")
        print("*")

        
    for i in range(largo):
        print("  * ", end="")

#7 Algoritmo 3N + 1

def secuencia():
    n = int(input())
    if n % 2 == 0:
        k = n / 2
        print(k)
    else:
        k = ( n*3) + 1
        print(k)





if __name__ == '__main__':
    ventana()
