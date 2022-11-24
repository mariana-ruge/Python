import os
os.system('cls')

'''
if condicion:
    #Codigo
    #Codigo
    #Codigo

#Codigo fuera del if
'''
def edad_computador():
    fabricacion = int(input("¿Cuántos años tiene tu computador?"))

    #Evaluar la primera clausula
    if fabricacion >= 0 and fabricacion <= 2:
        print("Tu computador es nuevo")
        print("Puedes continuar con tu PC")
    elif fabricacion < 0:
        print("Aún no has comprado el computador")
    else:
        print("Tu computador es viejo")
        print("Considera comprar uno nuevo")
    #Generar un espacio de líneas
    print('-' * 6)

def edad_conducir():
    edad = int(input("¿Cuál es tu edad?"))
    if edad <= 0:
        print("Error, la edad no puede ser negativa")
    elif edad >= 18:
        print("Puedes tener un permiso conducir")
    elif edad >= 16:
        print("Puedes conducir, pero sin permiso")
    elif edad >= 18 and edad <= 70:
        print("Puede conducir con licencia estándar")
    else:
        print("Requiere un estudio especial para conducir")

def contraseña():
    clave = "unarevolucion"
    datos = input(" Digite la clave ")
    convertida = datos.lower()
    if clave == convertida:
        print("Contraseña correcta")
    else:
        print("Contraseña incorrecta")

def precio_a_cobrar():
    cliente = input("¿Cuál es tu edad?")
    edad = int(cliente)
    if edad < 4:
        print("Entrada gratis")
    elif edad >= 4 and edad <= 18:
        print("Su tarifa es de 5000 pesos")
    else:
        print("Su tarifa es de 10000 pesos")


if __name__ == '__main__':
    precio_a_cobrar()