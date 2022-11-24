import os
os.system('cls')

def agenda():
    #persona = ["Carlos"]
    persona = {"Nombre":"Carlos", 
            "Telefono":"123456", 
            "Dirección": "Calle falsa avenida 123",
            "a":"el valor de a"}
    #print(persona)

    print(persona["Nombre"], persona["Telefono"], persona["Dirección"])

    print(persona["a"])

    print(persona.get("Dirección"))


#Pedir un número entero positivo
def diccionario_1():
    n = int(input("El número:"))
    while n < 1:
        if(n<1):
            print("El numero debe ser positivo")

    diccionario = {}
    for i in range(1,n+1):
        diccionario[i]= i**2

    print("Resultado", diccionario)

#Recibir como parametros una cadena, y devuelva el numero de repeticiones de cada caracter en la cadena

def contar_cadena(cadena):
    resultado = {}
    for letra in cadena:
        resultado[letra] = cadena.count(letra)

    return resultado

def run():
    print(contar_cadena("PALABRA"))




