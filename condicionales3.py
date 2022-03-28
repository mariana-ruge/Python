'''
Hacer un programa que simule un cajero automático con un saldo
inicial de $1000
y tendrá las siguientes opciones:
1: Ingresar dinero en la cuenta
2: Retirar dinero de la cuenta
3: Mostrar dinero disponible
4: Salir
'''

saldo_total = 1000;

print("Tu saldo es de ", saldo_total);
print("\t. :MENU:.")
print("¿Qué deseas hacer?")
print("1. Ingresar saldo en la cuenta")
print("2. Retirar dinero de la cuenta")
print("3. Mostrar dinero disponible")
print("4. Salir")

opcion = int(input("Opción: "))

print()

if opcion == 1: 
    agregar = float(input("¿Cuánto dinero desea ingresar?"))
    saldo_total = (saldo_total + agregar)
    print(" Su nuevo saldo es ", saldo_total)
elif opcion == 2: 
    retirar = float(input("¿Cuánto dinero deseas retirar?"))
    saldo_total = (saldo_total- retirar)
    if saldo_total < retirar:
        print("Fondos insuficientes")
    else:
        print("su nuevo saldo es de", saldo_total)
elif opcion == 3:
    saldo_disponible = saldo_total;
    print(saldo_disponible)
elif opcion == 4:
    print("Usted ha cancelado la operación")
else: 
    print("La opción seleccionada no es válida")