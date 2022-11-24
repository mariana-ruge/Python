import os
os.system('cls')

lista_1 = ["Mariana", "Julio", 30109085]

#Estructura de la lista
print(lista_1)

#Imprimir un solo elemento de la lista
print(lista_1[0])

#Iterar elementos en una lista
for x in lista_1:
    print(x)

#Agregar el mismo elemento a lista
print(len(lista_1))
lista_1.append("Calle Falsa, Avenida 1, 2, 3")

for y in lista_1:
    print(y)

print(len(lista_1))

#Agregar elementos a la lista con un input
dias_laborales = ['Lunes', 'Martes', 'Miercoles', 'Viernes']
nuevo_dia = dias_laborales.append(input())
print(dias_laborales)

#Eliminar elementos de una lista
primer_semestre = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio"]
primer_semestre.pop(5)
print(primer_semestre)
#pop lista.pop(1)

#Iterar en una lista
cadena = input("Digita una cadena")
dividir = cadena.split()
print(dividir)
for x in range(len(dividir)-1, -1, -1):
    if dividir[-1] == "a":
        lista_1.pop(x)

print(lista_1)

#Usando del/remove en una lista
frase = input("Digita otra cadena")
separar = frase.split()
print(separar)

del separar[1]

#Metodo remove
for x in separar:
    if x == "a":
        separar.remove(x)

print(separar)

#Modificar elementos de una lista
linea = input("Digita una frase")
list_2 = linea.split()
for x in range(len(list_2)):
    if list_2[x] == "Hola":
        list_2[x] = "Adiós"

print(list_2)