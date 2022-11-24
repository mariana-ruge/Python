def lectura_de_datos():
    N = int(input())
    db = [N]
    for i in range(N):
        c = input()
        db.append(c.split(' '))
    return db


def comparacion (db):
    disponibilidad = False
    bicicletas_aprobadas = []
    p1 = 240
    p2 = 300
    p3 = 160
    p4 = 180
    p5 = 240
    p6 = 275
    p7 = 50

    parametros = [p1, p2, p3, p4, p5, p6, p7]

    for i in range(db[0]):
        if (int(db[i+1][0]) >= parametros[0]) and \
            (int(db[i+1][0]) <= parametros[1]) and \
            (int(db[i+1][1]) >= parametros[2]) and \
            (int(db[i+1][1]) <= parametros[3]) and \
            (int(db[i+1][2]) >= parametros[4]) and \
            (int(db[i+1][2]) <= parametros[5]) and \
            (int(db[i+1][3]) <= parametros[6]):
            disponibilidad = True
            bicicletas_aprobadas.append(int(db[i+1][4]))

    if not disponibilidad:
            return["NO DISPONIBLE"]
    else:
            return bicicletas_aprobadas 


def imprimir(salida):
    for i in salida:
       print(i)

g = lectura_de_datos()

Resultado = comparacion(g)
imprimir(Resultado)




            