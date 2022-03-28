#salidas de datos

nombre = "Mariana";
edad = 17;

print("Hola" , nombre , "tienes", edad, "años");

#Metodo format para concatenar
print("Hola {} tienes {} años".format(nombre, edad));

#Concatenar con la F
print(f"Hola {nombre} tienes {edad} años");

#Entrada de datos

#Cadenas de texto
#Input guarda datos tipo cadena
usuario = input("Digita tu nombre: ");

print(f"Hola {nombre}");

#Numero
#Se usa int(input("Haz alguna cosa acá"))
numero = int(input("Digite un número: "));
print(f"El número es {numero + 1}");
decimal = float(input("Digita un décimal"));
print(f"El decimal es: {decimal}");