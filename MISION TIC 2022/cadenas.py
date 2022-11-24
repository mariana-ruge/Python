import os
os.system('cls')


print('""')
print("Hola")
print("Comilla simple ' ")
print('comilla doble " ')
print(" '\' ")

#Convertir un string en una lista
#El método split separa las cadenas de texto
cadena = "Tres tristes tigres tragaban trigo en un trigal"
dividir = cadena.split()
print(dividir)
print(type(dividir))
print(dividir[2])

#El método count indica cuantas veces aparece una palabra en una cadena
print("Numero de veces en una cadena")
trabalenguas = "Compadre, cómpreme un coco; compradre no compre coco; compadre, coco no compro. Que el poco coco come. Poco coco compra, y como poco coco compro, poco coco compro"
print(trabalenguas.count("coco"))

#Método index determina la posición de una palabra en la cadena
print("posición en la cadena")
saludo = "Hola mundo"
print(saludo.index("Hola"))
cancion = "Es cierto que hay que estar alerta y preparado para enfrentar peligros que nos puedan lastimar, pero siempre puede haber en vilo y acechando, tiburones en el bosque y zorros en el mar"
palabras = cancion.split()
print(palabras)
print(palabras.index("alerta"))

#Para convertir en mayúsculas y minúsculas
mensaje = "Esto es un mensaje secreto"
mayuscula = mensaje.upper()
print(mayuscula)

grito = "NO ESTOY GRITANDO"
minuscula = grito.lower()
print(minuscula)

#Cambiar las mayúsculas por minúsuculas 
tipico = "HoLa MuNdo"
cambio = tipico.swapcase()
print(cambio)

#Las funciones strip(), lstrip(), y rstrip() remueven los espacios en blanco que posea una cadena 
espacios = " Esta cadena tiene espacios en blanco "
remover = espacios.strip()
print(remover)

#El método replace remplaza una cadena por otra
saludo = "Hola estudiante"
saludo.replace("estudiante", "nombre")
print(saludo)