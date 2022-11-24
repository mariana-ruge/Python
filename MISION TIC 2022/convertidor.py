import os
os.system('cls')
#Se debe realizar un programa que convierta pesos a dólares o dólares a pesos

#Para convertir de pesos a dólares
valor_dolar = 4000
pesos = int(input("¿Cuántos pesos tienes?: "))
dinero_convertido = pesos/valor_dolar
print(" Tienes ", dinero_convertido, "dolares")

#Para convertir de pesos a euros
valor_euro = 4050
pesos_a_euro = pesos/valor_euro
euro = round(pesos_a_euro, 2)
print("Tienes ", euro, "euros")

