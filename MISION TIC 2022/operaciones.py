import os
os.system('cls')
#Leer 2 números, si son iguales, que los multiplique, si el primero es mayor  que el segundo que los reste, sino que los sume
num_1, num_2 = input().split()
num_1 = int(num_1)
num_2 = int(num_2)

if num_1 == num_2:
    a = num_1 * num_2
    print(a)
elif num_1 > num_2:
    b = num_1 - num_2
    print(b)
else:
    c = num_1 + num_2
    print(c)