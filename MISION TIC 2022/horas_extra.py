import os
os.system('cls')

'''
Determinar la cantidad de dinero que recibirá un trabajador por concepto de las horas trabajadas en la empresa
sabiendo que cuando las horas de trabajo exceden de 40, el resto se consideran horas extra y que estas se pagan
al doble de una hora normal sino exceden de 8, si las horas exceden de 8 se pagan las primeras 8 al doble y las 
que sobren al triple
'''

#determinar cuantas horas ha trabajado
#si las horas exceden de 40 pero son menores a 48
#   se paga al doble de la hora normal
# sino entonces
#   mientras horas sean menores a 56, se paga al doble
#  cuando horas sean mayores a 56, se pagan al triple

horas_trabajadas = int(input())
if horas_trabajadas < 0:
    print("Error, las horas no pueden ser negativas")
elif horas_trabajadas > 40 and horas_trabajadas < 48:
    print("dobles")
elif horas_trabajadas > 56 and horas_trabajadas <64:
    print("dobles + 1")
else:
    print("triples")