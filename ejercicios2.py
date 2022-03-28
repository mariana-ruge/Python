#Reescribe el programa del salario usando try y except, de modo que el
#programa sea capaz de gestionar entradas no numéricas con elegancia, mostrando
#un mensaje y saliendo del programa. 

'''

horas = input("Ingresar horas")
tarifa = input("Ingresar salario")

try:
 horas_flotantes = float(horas)
 tarifa_flotante = float(tarifa)
except:
    print("No has ingresado un número")
    quit()


if horas_flotantes > 40:
    reg = tarifa_flotante * horas_flotantes
    otp = (horas_flotantes - 40.0) * (tarifa_flotante * 0.5)
    xp = reg + otp
else:
    xp = horas_flotantes * tarifa_flotante

print(" Paga: " , xp)
'''

'''
Ejercicio 3: Escribe un programa que solicite una puntuación entre 0.0 y 1.0. Si la
puntuación está fuera de ese rango, muestra un mensaje de error. Si la puntuación
está entre 0.0 y 1.0, muestra la calificación usando la tabla siguiente:


nota = float(input("Digita una calificacion"))

if nota >= 0.9:
    print("Tu nota fue sobresaliente")
elif nota >= 0.8:
    print("Tu nota fue notable")
elif nota >= 0.7:
    print("Tu nota fue buena")
elif nota >= 0.6:
    print("Tu nota fue suficiente")
else:
    print("Tu nota es insuficiente")
'''

'''
Reescribe el programa de cálculo del salario, con tarifa-ymedia
para las horas extras, y crea una función llamada calculo_salario
que reciba dos parámetros (horas y tarifa).
'''
 
'''
def computepay (horas, tarifa) :
    #print("In computepay", horas, tarifa )
    if horas > 40 :
        parcial = tarifa * horas
        tasa = (horas - 40.0) * (tarifa * 0.5)
        total = parcial + tasa
    else: 
        total = horas  * tarifa
    
    return(total)


tiempo = input("Ingresa las horas:")
tarifa_x_hora = input("Ingresa la tarifa")
tiempoFlotante = float(tiempo)
tarifaFlotante = float(tarifa_x_hora)

total = computepay(tiempoFlotante, tarifaFlotante)

print("Pagas", total)

'''



