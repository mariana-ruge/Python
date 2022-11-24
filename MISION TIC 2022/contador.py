import os
os.system('cls')

def contar():
    diccionario = {"a": 1, "b": 2, "c": 3}

    lista = ["a", "b", "c", "d"]

    for count, valor in enumerate(lista):
        print("Llave ", count)
        print("Valor ", valor)


    for llave, valor in diccionario.items():
        print("Llave", llave)
        print("Valor", valor)
        
    numeros = ["1", "2", "2", "4", "2"]
    print(numeros.pop(0))

    #Tamaño de la memoria
    #Tamaño de los datos
    #Cambiar los datos por la iteración

    palabra = input()
    longitud = len(palabra)
    print(longitud)

def pedir_palabra():
    palabra = input("Palabra: ").upper()
    if len(palabra) % 2 != 0:
        return palabra
    else:
        print("La palabra debe ser impar")
        pedir_palabra()

def mostrar_centro(palabra):
    centro = len(palabra)//2
    print(palabra[centro])

if __name__ == "__main__":
    mostrar_centro(pedir_palabra())
    