import os
os.system('cls')
#input: salario_base, cantidad_horas_extras.
salario, horas_extra, bonificacion = input().split()

#Convirtiendo los tipos de datos
salario = float(salario)
horas_extra = float(horas_extra)
bonificacion = int(bonificacion)

#Calculando el valor de la hora
valor_hora = salario / 192
#Calculando las horas extras
#Como se necesita el valor de la hora extra incrementado se multiplica por el 1.25%
valor_extra = valor_hora * 1.25
#Calculando la bonificacion
valor_bonificacion = salario * 0.05

#Plantear operaciones
#Sacando el salario total
salario_total = salario + horas_extra * valor_extra + bonificacion * valor_bonificacion

#Estableciendo descuentos de Ley
descuentos = (salario_total * 0.04) + (salario_total * 0.035) + (salario_total * 0.01)

#Calcular el salario a pagar
salario_a_pagar = salario_total - descuentos
salario_redondo = round(salario_a_pagar, 1 )

print(salario_redondo)