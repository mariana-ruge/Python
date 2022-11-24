Nombre = 0
Telefono = 0
Direccion = 0
def run():
    n = int(input("Numero de personas: "))
    agenda = []
    for i in range(n):
        persona = input("Datos Personales: ").split(',')
        agenda.append(persona)

    #mostrar_agenda(buscar_x_nombre(agenda, "Robert"))

def buscar_x_nombre(agenda,nombre):
    resultados = []
    for persona in agenda:
        if persona in agenda:
            if persona[Nombre] == nombre:
                resultados.append(persona)
    return resultados

def mostrar_agenda(agenda):
    for persona in agenda:
        print("Nombre", persona[Nombre], "Telefono:", persona[Telefono], "Direccion:", persona[Direccion])
