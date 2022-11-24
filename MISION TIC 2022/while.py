import os
os.system('cls')
#Numero indetermida de operaciones

#Modificar la condicion del while para evitar terminar en un
#bucle infinito.

a = 0

#ciclo positivo
while a < 100:
    a = a + 1
    print(a)

print("Fin del ciclo")
 
b = 1

#ciclo negativo
while b <= 50:
    b = b - 1
    print(b)
    if b < -50:
        break

#cortar ciclos
sueldo = 100000

while sueldo >= 150000:
    sueldo = sueldo - 1000
    print("Apto para compras")
    if sueldo < 100000:
        break
    print("Se esta acabando el dinero")

c = 0

#Otro ciclo
while c <= 100:
    c += 1
    if c % 2 == 0:
        continue
    print(c)
print("Fin del bucle")

