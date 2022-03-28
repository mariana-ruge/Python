#Escribir una expresión algebraica de forma algoritmica
"""""
a = float(input(" Digita el valor de a: "))
b = float(input(" Digita el valor de b: "))
c = float(input(" Digita el valor de c: "))

resultado = float(a**3 * (b**2 - 2 * a * c)) / (2*b);
print(resultado);
"""""

#Determinar la solucion logica de la siguiente operacion

""""
a = float(input("Digita el valor de a: "))
b = float(input("Digita el valor de b:" ))


d =((3 + 5 * 8) < 3 and ((-6/3*4) + 2 < 2)) or (a>b)

print(d);
"""

#Escriba  un programa para calcular el salario bruto
"""
horas = float(input(" Ingresar Horas: "));
tarifa = float(input("Ingresa la tarifa: "));

salario = horas * tarifa;
print(' salario ', salario);
"""

#Escribe un programa que use input para pedirle al usuario su nombre y luego darle la bienvenida
"""
nombre = input(" ¿Cuál es tu nombre? ");
bienvenida = print(" Hola " , nombre);

"""



#Operaciones en variables
"""
ancho = 17
alto = 12.0

d = ancho/2
print(d)
e = ancho/2.0
print(e)
a = alto/3
print(a)
k = 1 + 2 * 5
print(k)


"""
#Escribe un programa que le pida al usuario una temperatura en grados Celsius, la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida.

"""
temperatura = int(input("¿Cuál es tu temperatura?"))
fahrenheit = ((temperatura * (9 / 5)) + 32)
print(fahrenheit)
"""

#Reescribe el programa del cálculo del salario para darle al empleado 1.5 veces la tarifa horaria para todas las horas trabajadas que excedan 40

horas = float(input(" Ingresar Horas: "));
tarifa = float(input("Ingresa la tarifa: "));
flotar_horas = float(horas);
salario_por_hora = float(tarifa);


if flotar_horas > 40 :
    tarifa = tarifa * 1.5
    salario = horas * tarifa;
    print ('El salario con recargo es' , salario)
    
else:
    print('No se ha cambiado la tarifa')
    salario = horas * tarifa;
    print(' salario ', salario);








