import os
os.system('cls')
#Entradas: distancia(m), vel_max(km/h), tiempo(s)
#Salida: "OK", "Multa", "Curso de Sensiblización" "Error"
#Proceso: 1- Leer distancia, vel_max, tiempo
#         2- si distancia < 0 o vel_max < 0 o tiempo <0
#              imprimir: "ERROR"
#         Sino entonces:
#         3- tiempo = tiempo/3600 (horas)           
#         4- distancia = distancia/1000 (km)           
#         5- velocidad = distancia/tiempo
#         6- vel_multa = vel*1.20
#         7- si vel <= vel_max entonces:
#            imprimir "OK"
#         8- sino vel < vel_multa entonces:
#             imprimir "MULTA"
#         9- sino entonces:
#            imprimir "CURSO"

distancia, vel_max, tiempo =  input().split()
distancia =  int(distancia)
tiempo = int(tiempo)
vel_max = int(vel_max)

if distancia < 0 or vel_max < 0 or tiempo < 0:
    print("ERROR")
else:
    tiempo = tiempo/3600
    distancia = distancia/1000
    velocidad = distancia/tiempo
    vel_multa = vel_max*1.20
    if velocidad < vel_max:
        print("OK")
    elif velocidad >= vel_max and velocidad <= vel_multa:
        print("MULTA")
    elif velocidad > vel_multa:
        print("CURSO DE SENSIBILIZACION")
