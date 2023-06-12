import os
os.system('cls')
import random
import string
from vidas_diccionario_ahorcado import vidas_diccionario_visual

#Lista de palabras disponibles
palabras = ['aire', 'ojos', 'piel', 'alto', 'calor', 'colores', 'nubes', 'sol', 'negro', 'blanco', 
            'piramide', 'secretos', 'universo', 'amarillo', 'azul', 'rojo', 'gris', 'estrellas', 'galaxias',
            'noche', 'dia', 'cargador', 'audifonos', 'bloc', 'teclado', 'cable', 'python', 'gris', 'fuego',
            'pizza', 'sonido', 'dentista', 'gafas', 'joven', 'reloj', 'saltar', 'escritor','vivir', 'locura',
            'tienda', 'tres', 'tristes', 'tigres', 'tragaban', 'trigo', 'en', 'un', 'trigal', 'cubo', 'piramide',
            'esfera', 'volumen', 'nubes', 'fisica', 'luna', 'cama', 'almohada', 'dibujar', 'artista', 'distosion',
            'pino', 'arbol', 'zapato', 'pera', 'banano', 'manzana', 'camiseta', 'cabello', 'caballo', 'mesa', 'festivo',
            'navidad', 'programar', 'computacion', 'cubo', 'lechuza', 'celular', 'android', 'falla', 'dinosaurio', 'castillo',
            'cuaderno', 'libro', 'archivo', 'correo', 'escritorio', 'icono', 'acceder', 'identidad', 'digitar']
    

def obtener_palabra(palabras):
    #Seleccionar una palabra al azar de la lista de palabras válidas
    palabra = random.choice(palabras)

    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabra)

    return palabra.upper()



def ahorcado():
    print("***Bienvenido al ahorcado en Python***")
    #Obtener la palabra 
    
    palabra = obtener_palabra(palabras)

    letras_por_adivinar = set(palabra)
    abecedario = set(string.ascii_uppercase)
    #ascii tiene todas las letras de python (en inglés)
    letras_adivinadas = set()

    #Los conjuntos no admiten caracteres repetidos, se declaran con set y los parentesis
    vidas = 7

    #Lógica principal del juego
    #Método join une todas las secuencias

    #Letras adivinadas
    #'.'join({'A', 'B', 'C})

    while vidas > 0 and len(letras_por_adivinar)>0:
        print(f"Te quedan estas {vidas} vidas y has usado {''.join(letras_adivinadas)}")

        #Mostrar el estado actual de las palabras
        #List Comprenhenshion, listas por comprension
        lista_palabras = [letra if letra in letras_adivinadas else ' ' for letra in palabra]
        #Mostrar el estado del ahorcado
        print(vidas_diccionario_visual[vidas])
        print(f"Palabra: {'_'.join(lista_palabras)}")

        #Escoger una letra nueva
        letra_usuario = input("Escoge una letra: ").upper()

        #Si la letra escogida por el usuario está en el abecedario, y no está en el conjunto de letras ingresado
        #Se añade la letra al conjunto de letras ingresadas
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)

            #Verificar si la letra está en la palabra
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            else:
                #Si la letra no está en la palabra, se resta una vida
                vidas -= 1
                print(f"\n Tu letra {letra_usuario} no está en la palabra. ")
        elif letra_usuario in letras_adivinadas:
            #Si la letra escogida por el usuario ya fue ingresada 
            print('\n Ya escogiste esa palabra, por favor, escoge una letra nueva')
        else:
            print('Pusiste un caracter no válido')       

    #El juego llega hasta aquí cuándo se adivina la palabra o cuándo se quedó sin vidas
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"Has sido Ahorcado, perdiste. La palabra era: {palabra}")
    else:
        print(f'Has ganado el ahorcado, adivinaste el palabra: {palabra}')

    
ahorcado()





