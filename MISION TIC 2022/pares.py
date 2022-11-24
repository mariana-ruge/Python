import os
os.system('cls')
#Determinar si los números son pares o impares
def pares():
    numero = int(input(" Digita un número "))
    if numero % 2 == 0:
        print("Es par")
    else:
        print("Es impar")

'''
= --> Asignar
== --> comparar
'''
if __name__ == "__main__":
    pares()
