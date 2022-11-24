import os
import random
os.system('cls')

glosario = ["SOL", "SAL", "AGUA", "TIERRA"]
secreto = ""
def generar_palabra():
    global secreto
    secreto = random.choice(glosario)

def pedir_letra():
    letra = input("Letra: ")
    if len(letra) != 1:
        print("Solo debe escribir 1 letra")
        letra = pedir_letra()
    else:
        pass

def mostrar_secreto():
    print("__".join(secreto))

def run():
    pass

if __name__ == "__main__":
        pedir_letra()