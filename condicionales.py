'''
numero = int(input("Digite un número: "))

if numero > 0:
    print("El numero es positivo")
elif numero == 0:
    print("El numero es neutro")
else:
    print("El numero es negativo")
'''

'''
#Condicionales combinados

edad = int(input("Digita tu edad"))

if edad > 0 and edad < 110:
    print("Edad correcta")
    if edad >= 18:
        print("Eres mayor de edad")
    else:
        print("No es mayor de edad")
else:
    print("No se ha digitado una edad correcta")
'''

'''
#Hacer un programa que determine cuál número es mayor
primero = int(input("Ingresa un número"))
segundo = int (input("Ingresa otro número"))

if primero > segundo:
    print(" El numero mayor es ", primero)
else:
    print(" El numero mayor es ",  segundo)
'''

'''
#Hacer un programa que pida 2 números y se de cuenta de cuál de ellos es par o si ambos lo son

numero_uno = int(input("Ingresa un número"))
numero_dos = int(input("Ingresa otro número"))

if numero_uno % 2 == 0 and numero_dos%2 == 0:
    print("Ambos son pares")
elif numero_uno % 2 == 0 and numero_dos % 2 != 0:
    print(f"{numero_uno} es par")
elif numero_uno % 2 != 0 and numero_dos % 2 == 0:
    print(f"{numero_dos} es par")
else:
    print("Ambos números son impares")

'''

'''
Hacer un programa que nos pida 3 números y determine cual es el mayor
'''
'''
num1 = int(input("Digita  un numero"))
num2 = int(input("Digita  un numero"))
num3 = int(input("Digita  un numero"))

if num1 >= num2 and num1 >= num3:
    print(f"El número mayor es {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"El número mayor es {num2}")
elif num3>=num1 and num3>=num2:
    print(f"El número mayor es {num3} ")
'''

'''
Ejercicio 3:
Hacer un programa que pida un caracter e indique si es una vocal o no.
'''

'''
letra = input("Digita una letra: ").lower()

if letra == 'a' or letra == 'e' or letra  == 'i' or letra == 'o' or letra == 'u':
    print("Es una vocal")
else:
    print("No es una vocal")

'''

'''
Funcionamiento de la calculadora

a = float(input("Digita un número"))
b = float(input("Digita otro número"))

operador = 0
while True:
    print("¿Qué vamos a hacer?")
    print("""Estás son las opciones
    
    1) Sumar los 2 números
    2) Restar los dos números
    3) Multiplicar los dos números
    4) Dividir los dos números
    5) Apagar la calculadora

    """)

    opcion = int(input("Elige una opción: ") )     

    if opcion == 1:
        print(" ")
        print("=", a + b)
    elif opcion == 2:
        print(" ")
        print("=", a - b)
    elif opcion == 3:
        print("")
        print("=", a * b )
    elif opcion == 4:
        print("")
        print("=", a / b)
    elif opcion == 5:
        break
    else:
        print("No se ha seleccionado una opción")
'''

#Dado un número entero, muestra el valor absoluto

'''
numero = int(input("Digita un número"))
if numero >= 0:
    valor = numero * 1
    print(f"El valor absoluto es {valor}")
else:
    valor = numero * -1
    print(f"El valor absoluto es {valor}")
'''

'''
Ingresar el nombre de dos personas, los cuales se almacenaran
en dos variables.
Imprimir conincidencia si los nombres de ambas personas comienzan
con la misma letra o si terminan con la misma letra
si no es así, imprimir no hay coincidencia
'''
n1 = input("Ingresa el primer nombre")
n2 = input("Ingresa el segundo nombre")

if n1[0] == n2[0] or n1[-1] == n2[-1]:
    print("Coincidencia")
else:
    print("No coincidencia")