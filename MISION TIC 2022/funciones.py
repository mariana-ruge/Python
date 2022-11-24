#Las funciones son formas de encapsular código en python
#Las funciones generan código reutilizable, es decir, que puede ser ejecutado varias veces
#Se usa la sentencia def, y el código del bloque estará identado

import os 
os.system('cls')

def operacion(num1, num2):
    resultado = num1 * num2
    return resultado

#print(operacion(5, 10))

def dentro_fuera():
    x = 0
    y = 1
    e1 = list(map(float, input()))
    e2 = list(map(float, input()))
    p = list(map(float, input()))
    if esta_rango(e1[x], e2[x], p[x]) and \
        esta_rango(e2[y], e1[y], p[y]):
        print("SI")
    else:
        print("NO")

def esta_rango(xi, xf, p):
    return True if xi >= p <= xf else False

#Funcion main para ejecutar código, puesto que en python todo debería estar dentro de funciones
if __name__ == "main":
    dentro_fuera()

