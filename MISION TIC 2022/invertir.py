import os
os.system('cls')
#Invertir cadena

str = input("Digita la palabra")
str_al_reves='' #Cadena vacía
i = len(str) #tamaño del string
while i > 0: 
    str_al_reves += str[i-1]
    i = i - 1 #bajar el índice
print("La cadena al revés", str_al_reves) 