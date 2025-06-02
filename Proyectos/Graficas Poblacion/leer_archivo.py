import os
os.system('cls')
import csv
def leer_archivo(ruta):
    with open(ruta, 'r') as csvfile:
        lector = csv.reader(csvfile, delimiter=',')
        cabecera = next(lector)
        data = []
        for columna in lector:
            iterable = zip(cabecera, columna)
            paises_diccionario = {key:value for key, value in iterable}
            data.append(paises_diccionario)
    return data


if __name__ == '__main__':
    data = leer_archivo('poblacion\world_population.csv')
    print(data[0])
    paises = list(map(lambda x: x['Country/Territory'], data))
    print(paises)
