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
    elif velocidad >= vel_max and velocidad < vel_multa:
        print("MULTA")
    else:
        print("CURSO SENSIBILIZACION")