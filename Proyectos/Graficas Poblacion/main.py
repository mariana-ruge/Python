import utils
import leer_archivo
import tablas

def run():
    data = leer_archivo.leer_archivo('./poblacion\world_population.csv')
    data = list(filter(lambda item: item['Continent']== 'South America', data))

    paises = list(map(lambda x: x['Country/Territory'], data))
    porcentajes = list(map(lambda x: float(x['World Population Percentage']), data))
    tablas.generar_grafica_barras(paises, porcentajes)
    tablas.generar_grafica_pie(paises, porcentajes)

run()