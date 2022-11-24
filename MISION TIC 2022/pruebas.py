import os
os.system('cls')

print("Hola Mundo")
x = int(input())
y = int(input())
print("suma es", x + y)
print("aquí finaliza el código")

#Ejercicios de python
N1,N2,N3=input().split()
N1=float(N1)
N2=float(N2)
N3=float(N3)

if N1>=N2 and N1>=N3:
    print(N1)
elif N2>=N1 and N2>=N3:
    print(N2)
elif N3>=N1 and N3>=N2:
    print(N3)
