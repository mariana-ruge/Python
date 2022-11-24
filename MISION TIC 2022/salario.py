import os
os.system('cls')

#Entradas: valor_hora, horas_trabajadas
#Salidas: salario
#Proceso:
#       1- Leer valor_hora, horas_trabajo
#       2- horas_triples = horas_trabajo - 48
#       3- si horas_triples < 0:
#               horas_triples = 0
#       4- horas dobles = horas_trabajo - 40 - horas_triples
#       5- si horas_dobles < 0:
#             horas_dobles = 0
#       6- horas_normales = horas_trabajo - horas_dobles - horas_triples
#       7- salario = (horas_normales*valor_hora) + (horas_dobles*valor_hora*2) + (horas_triples*valor_hora*3)

valor_hora, horas_trabajadas = input().split()
valor_hora = float(valor_hora)
horas_trabajadas = float(horas_trabajadas)

horas_triples = horas_trabajadas - 48
if horas_triples < 0:
    horas_triples = 0

horas_dobles = horas_trabajadas - 40 - horas_triples
if horas_dobles<0:
    horas_dobles=0

horas_normales = horas_trabajadas - horas_dobles - horas_triples

salario = (horas_normales*valor_hora) + (horas_dobles * valor_hora * 2) + (horas_triples * valor_hora * 3)
print(salario)


