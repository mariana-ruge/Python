from math import factorial


import os
os.system('cls')
def factorial_for():
    numero = int(input("n: "))
    factorial = 1
    for i in range(numero, 0, -1):
        factorial *= i
    print(factorial)

factorial_for()