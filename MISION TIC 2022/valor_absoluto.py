import os
os.system('cls')
#Entrada: numero
#Salida: valor absoluto del número
#Proceso:
# si numero > 0
#       print(numero)
#else
#       absoluto = numero * -1
#       print(absoluto)

numero = int(input("Digita un número"))
if numero > 0:
    print(numero)
else:
    absoluto = numero * -1
    print(absoluto)