import os
os.system('cls')

def obtener_poblacion(pais_diccionario):
    pais_diccionario = {
        '2022': pais_diccionario['2022 Population'],
        '2020': pais_diccionario['2020 Population'],
        '2015': pais_diccionario['2015 Population'],
        '2010': pais_diccionario['2010 Population'],
        '2000': pais_diccionario['2000 Population'],
        '1990': pais_diccionario['1990 Population'],
        '1980': pais_diccionario['1980 Population'],
        '1970': pais_diccionario['1970 Population']
    }
    return pais_diccionario.keys(), pais_diccionario.values()

def obtener_poblacion_por_pais(info, pais):
    resultado = list(filter(lambda item: item['pais']== pais, info))
    return resultado

