import matplotlib.pyplot as plt

def generar_grafica_barras(etiquetas, valores):
    #Generar las gráficas de barras
    fig, ax = plt.subplots()
    ax.bar(etiquetas, valores)
    plt.show()

def generar_grafica_pie(etiquetas, valores):
    #Generar la gráfica de tipo pie
    fig, ax = plt.subplots()
    ax.pie(valores, labels=etiquetas)
    plt.show()

#Imprimir las gráficas de barras
if __name__ == '__main__':
    print('Gráfica de barras')
    etiquetas = ['Barra 1', 'Barra 2', 'Barra 3']
    valores = [150, 300, 100]
    generar_grafica_barras(etiquetas, valores)
    generar_grafica_pie(etiquetas,valores)