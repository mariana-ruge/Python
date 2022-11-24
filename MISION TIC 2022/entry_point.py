#El entry_point o punto de entrada
#Es el punto donde el lenguaje de programación ejecutará las
#primeras instrucciones de un programa y donde el programa
#Tiene accseso a los argumentos de la linea de comandos

#Declarando la funcion factorial
def factorial(n):
    c = n
    f = 1
    print(c)
    while(c > 0):
        if c>1:
            print(print(c))
        else:
            print(c ,"=")

        f *= c
        c -= 1

    print(f)
    return f

a = factorial(4)
print(a)

#El script que estamos ejecutando es el principal
print(__name__)

#Crear una función principal y llamar a la función principal en el main

#Por lo tanto lo que se pregunta acá es, si el nombre del script principal
#es igual al archivo principal, que ejecute la función
if __name__ == "__main__":
    factorial(6)