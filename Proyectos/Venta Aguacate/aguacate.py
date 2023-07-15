import os
os.system('cls')
import pandas as pd
import matplotlib.pyplot as plt

#Leer el archivo
data = pd.read_csv("proyecto_aguacate/avocado.csv")
print(data)

atlanta = data[data['region'] == 'Atlanta']

precio = atlanta['AveragePrice']
volumen = atlanta['Total Volume']

bolsasAguacate = atlanta['Total Bags']
sbolsas = atlanta['Small Bags']
lbolsas = atlanta['Large Bags']
xbolsas = atlanta['XLarge Bags']

#nfila, ncolumnas, índice
plt.subplot(221)
plt.title('Precio Aguacate')
plt.plot(precio, label='Price', color='#138D75')
plt.legend()

plt.subplot(222)
plt.title('Volumen de aguacates')
plt.plot(volumen, label='Total Volume', color='#BA4A00')
plt.legend()


plt.subplot(223)
plt.title('Bolsas totales de aguacate')
plt.plot(volumen, label='Total Bags', color='#2E86C1')
plt.legend()

plt.subplot(224)
plt.title('Bolsas por tamanio')
plt.plot(sbolsas, label='Bolsas S ', color='black')
plt.plot(lbolsas, label='Bolsas L', color='green')
plt.plot(xbolsas, label='Bolsas XL', color= '#4A235A')
plt.legend()


plt.show()
