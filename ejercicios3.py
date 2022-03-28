import math

'''
Hacer un programa que intercambie el valor de 2 variables

a = input("Digita el valor de a")
b = input("Digita el valor de b")


#Intercambiando ambas variables
a , b = b , a

print(' El nuevo valor de a es: ', a)
print('El nuevo valor de b es ', b)

'''

'''
Hacer un programa para ingresar el radio de un circulo y se 
reporte su area y longitud de la circunferencia
'''

'''
radio = float(input("¿Cual es el radio?"))
print(type(radio))

print("Este es el área")
area = math.pi * (radio**2)
print(area)
print("Esta es la longitud")
longitud = (2 * math.pi * radio)
print(longitud)

'''

'''
Una tienda ofrece un descuento del 15% sobre el total de la 
compra y un cliente desea saber cuánto deberá pagar finalmente
por su compra
'''
compra = float(input("Ingresa el total de la compra"))
descuento = (compra * 15) / 100

print(descuento)