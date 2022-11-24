import os
os.system('cls')
db = {"Manzana": 1500,"Limon":200}
fruta = input("Fruta: ")
cantidad = float(input("Cantidad: "))

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("cls")


def calcular_valor(fruta, cantidad):
    valor_unitario = db.get(fruta)

    if valor_unitario != None:
        total=db[fruta]*cantidad
    else:
        agregar_fruta(fruta)
        total = calcular_valor(fruta,cantidad)
    return total

def pedir_datos():
    fruta = input("Fruta: ")
    cantidad = float(input("Cantidad: "))
    print("Total a pagar:", calcular_valor(fruta, cantidad))

def otra_consulta():
    print("¿Quieres hacer otra consulta?")
    print("[s] --> sí")
    print("[N] --> No")
    respuesta = input("<--").upper()
    if respuesta in ("S", "N"):
        return True if respuesta == "S" else False
    else:
        return otra_consulta()

def agregar_fruta():
    print("Agregar fruta...")
    print("Nombre:", fruta)
    valor = int(input("Valor :"))
    db[fruta] = valor
    
def run():
    while True:
        clear_screen()
        pedir_datos()
        if not otra_consulta():
            break
    print("Hasta luego...")


if __name__ == "__main__":
    run()


