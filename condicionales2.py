'''
Crear un programa que le permita al usuario elegir un candidato
por el cual votar. Las posibilidades son: candidato A por el 
partido rojo, candidato B por el partido verde, candidato C por 
el partido azul
Según el candidato elegido (A, B o C) se le debe imprimir el 
mensaje "Usted ha votado por el partido [color que corresponda
al candidato elegido]

candidato_A = "Partido Rojo"
candidato_B = "Partido Verde"
candidato_C = "Partido Azul"

candidato_seleccionado = input(" Elige un candidato, A: Por el partido rojo, B: por el partido verde, C: por el partido azul: ")

if candidato_seleccionado == "A":
    print("Usted ha seleccionado el", candidato_A)
elif candidato_seleccionado == "B":
    print("Usted ha seleccionadoo el", candidato_B)
elif candidato_seleccionado == "C":
    print("Usted ha seleccionado el", candidato_C)
else:
    print("Opción errónea")
'''

'''
Hacer un programa que permita saber si un año es bisiesto.
Para que un año sea bisiesto debe ser divisible por 4 y no
debe ser divisible por 100, excepto que también sea divisible
por 400


año = float(input("Ingresa un año"))

if año % 4 == 0 and año % 100 != 0 or año % 400 == 0:
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")
'''