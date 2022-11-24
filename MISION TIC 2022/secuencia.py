import os
os.system('cls')
#3N + 1
#Se debe generar una secuencia de números.
#Se inicia con un entero n
#       Si el entero es par se debe dividir por 2
#       Si es impar se mutiplica por 3 y se suma 1
#El proceso se debe repetir con el nuevo valor generado
#Imprimir la secuencia hecha por el algoritmo


#Pasos para resolverlo
# pedir el números al usuario (n = input("Digite un número"))
# generar un ciclo para iterar hasta que n == 0
# Crear una lista para almacenar las secuencias
# secuencia = [] 
#mientras numero sea > 0:
#    Evaluar el número
#    si numero % 2 == 0
#       numero = numero/2
#    sino
#       numero = (numero*3)+1
#
# secuencia.append(numero)  

n = input("Digita un número")
numero = int(n)

for secuencia in range(numero):
    if numero % 2 == 0:
        numero = numero / 2
        print(numero)
    else:
        numero = (numero*3)+1
        print(numero)




