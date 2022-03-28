#Listas

lista = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]

'''
print(lista)
print(lista [0])
#Para ir en sentido contrario se usa el signo negativo
print(lista[-2])
print(lista[0:3])
print(lista[1:4])

'''


lista_dos = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio"]

#print(len(lista_dos))

numeros = [1, 2, 3, 4, 5, 6, 7, 8]
'''
numeros.append(9)
print(numeros)

'''

#Insert agregar un elemento a la lista
letras = ["a", "i", "o", "u"]
'''
letras.insert(1, "e")
print(letras)
'''


#Concatenar listas
enteros = [10, 20 ,30, 40, 50]
'''
enteros.extend([60, 70, 80, 90, 100])
print(enteros)
'''

#Sumar 2 listas
listaA = [3, 6, 9, 12, 15, 18, 21]
listaB = [2, 4, 6, 8, 10, 12, 14]

'''
listaC = listaA + listaB
print(listaC)
'''

#Buscar datos en la lista
datos = [88, 10, 21, 39, 33, 10, "Tom"]
'''
print( 88 in datos)
print(15 in datos)
'''

#Buscar el indice donde se encuentra el elemento
base = ["Andromeda", "Vía Láctea", "Palo de Hokey", "Supernova", "Nebulosa" ]
'''
print(base.index("Supernova"))
'''

#Buscar elementos que se repiten en una lista
turnos = [1, 2, 4, 7, 2, 9, 11, 1, 2, 3, 4, 5, 6, 2, 3, 5]
'''
print(turnos.count(2))
'''

#Como eliminar elementos de una lista

tareas = ["tarea uno", "tarea dos", "tarea tres", "tarea cuatro", "tarea cinco"]

'''
tareas.pop(2)
print(tareas)

tareas.remove("tarea cinco")
print(tareas)
'''

#Poner una lista al revés
voltear = ["acción", "cámara", "luces"]
'''
voltear.reverse()
print(voltear)
'''

#Duplicar la lista 
fotocopia = ["papas", "Hamburguesa", "Gaseosa"] * 2
'''
print(fotocopia)
'''

#Ordenar los elementos de la lista
enteros = [8, -7, 9, -15, 71, -10, 0, 1, 3]
enteros.sort()
'''
print(enteros)
'''

#Ordenar los números al revés
naturales = [9, 6, 7, 5, 3, 2, 4, 1, 8]
naturales.sort(reverse= True)
print(naturales)







