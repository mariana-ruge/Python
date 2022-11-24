import os
os.system('cls')
#El ciclo for se utiliza para recorrer elementos de un objeto iterable (lista, tupla, conjunto, diccionario, etc..)

#ciclo for con un string
def for_en_string():
    for x in "Hola":
        print(x)

for_en_string()

#ciclo for en una lista
def for_en_lista():
    lista = [1,2,3,"hola", 2.90]
    for x in lista:
        print(x)

print(list(range(10)))
print(list(range(1,8)))
print(list(range(0, 100, 10)))
#range(número de partida, número de fin, la "cuenta")

print("--->", list(range(0,11,2)))
print("-->", list(range(1,11,2)))

#Iteraciones de for
for i in range(10):
    print(i)
    if i == 5:
        break

