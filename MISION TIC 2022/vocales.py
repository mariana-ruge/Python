import os
os.system('cls')

vocales = ["a", "e", "i", "o", "u"]
frase = input("La Frase : ").lower()
contador_vocales = 0

for letra in frase:
    if letra in vocales:
        #es vocal
        contador_vocales += 1

print("Tiene", contador_vocales, "vocales")