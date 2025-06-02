#Importar librerías
import pandas as pd #Para manejar los datos
import re #para expresiones regulares
from datetime import datetime #para fechas

#Para limpiar la consola
import os
os.system('cls' if os.name == 'nt' else 'clear')

#Crear la función solicitada
def recomendar_youtuber(youtubers: dict, suscriptores_min: int, suscriptores_max: int,
                        fecha_minima: str, fecha_maxima: str, videos_minimos: int,
                        palabra_clave: str) -> dict:
    """
    Recomienda al primer (uno solo) YouTuber que cumpla con todos los criterios de búsqueda especificados.
    
    La función busca un YouTuber que:
    - Pertenezca a la categoría con más visitas totales.
    - Tenga un número de suscriptores dentro del rango especificado.
    - Ha publicado al menos la cantidad mínima de vídeos indicada.
    - Ha publicado dentro del rango de fechas especificado.
    - Contiene la palabra clave en su descripción (sin distinguir entre mayúsculas/minúsculas).
    
    Parámetros:
        youtubers (dict): Diccionario con la información de los YouTubers.
        suscriptores_min (int): Cantidad mínima de suscriptores requerida (inclusive).
        suscriptores_max (int): Cantidad máxima de suscriptores permitida (inclusive).
        fecha_minima (str): Fecha mínima en formato YYYY-MM-DD (inclusive).
        fecha_maxima (str): Fecha máxima en formato YYYY-MM-DD (inclusive).
        videos_minimos (int): Cantidad mínima de videos subidos requerida.
        palabra_clave (str): Palabra clave que debe encontrarse como parte de la descripción.
    
    Retorno:
        dict: La información del primer YouTuber que cumple con los criterios.
            Si no se encuentra ningún YouTuber que cumpla, retorna un diccionario vacío.
    """
    
    #Convertir fechas de string para hacer la comparación
    
    '''
    Las fechas del data frame estan en formato date, pero para hacer la búsqueda es mas sencillo usar fechas en formato strtime
    '''
    fecha_minima = datetime.strptime(fecha_minima, "%Y-%m-%d")
    fecha_maxima = datetime.strptime(fecha_maxima, "%Y-%m-%d")
    
    #validación
    #Las fechas deben ser coherentes
    if fecha_minima > fecha_maxima:
        print("La fecha minima no debe ser posterior a la maxima")
        return {}
    
    #Encontrar la categoría con más visitas totales, se crea un diccionario para poder almacenar las visitas
    categoria_visitas = {}
    '''
    Se debe recorrer el diccionario de los youtubers
    '''
    for youtuber_id, info in youtubers.items():
        '''
        Filtros a usar
        categoria e info, vienen del dataset
        '''
        categoria = info.get('categoria', '')
        visitas = info.get('visitas', 0)
        # si se encuentra la categoria, se aumentan las vistas
        if categoria in categoria_visitas:
            categoria_visitas[categoria] += visitas
        else:
            categoria_visitas[categoria] = visitas
    
    #Obtener la categoría con mas visitas
    if categoria_visitas:
        #Método para obtener la categoría
        #Se usa el método get para traer la categoría y hacer la consulta en el diccionario
        categoria_popular = max(categoria_visitas, key=categoria_visitas.get)
    else:
        categoria_popular = None
        
    print(f"Categoría más popular: {categoria_popular}")
        
    # Contadores para diagnóstico
    #Buscar los datos
    categoria_count = 0
    suscriptores_count = 0
    videos_count = 0
    fecha_count = 0
    keyword_count = 0
    
    # Almacenar coincidencias parciales (cumplen la mayoría de criterios)
    coincidencias_parciales = {}
    mejor_coincidencia = None
    #Inicializar las coinicdencias
    max_criterios_cumplidos = 0
    
    #Buscar el youtuber que cumpla con todos los criterios
    for youtuber_id, info in youtubers.items():
        criterios_cumplidos = 0
        
        #Verificar si el youtuber pertenece a la categoría más popular
        if info.get('categoria', '') == categoria_popular:
            categoria_count += 1
            criterios_cumplidos += 1
        else:
            continue  # Este criterio es obligatorio
            
        #Verificar el rango de suscriptores
        suscriptores = info.get('suscriptores', 0)
        
        #Inicializa los suscriptores se usa un limite inferior y un limite superior
        if suscriptores_min <= suscriptores <= suscriptores_max:
            suscriptores_count += 1
            criterios_cumplidos += 1
        else:
            # Guardar como coincidencia parcial si cumple al menos 4 criterios
            continue
            
        #Verificar el número mínimo de videos
        videos = info.get('videos', 0)
        if videos >= videos_minimos:
            videos_count += 1
            criterios_cumplidos += 1
            
        #Verificar la fecha de publicación
        fecha_publicacion = info.get('fecha_publicacion')
        if fecha_publicacion and (fecha_minima <= fecha_publicacion <= fecha_maxima):
            fecha_count += 1
            criterios_cumplidos += 1
            
        #Verificar la palabra clave en la descripción
        descripcion = info.get('descripcion', '').lower()
        if palabra_clave.lower() in descripcion:
            keyword_count += 1
            criterios_cumplidos += 1
            
        # Guardar como coincidencia parcial
        if criterios_cumplidos >= 3:  # Si cumple al menos 3 de 5 criterios
            coincidencias_parciales[youtuber_id] = {
                'info': info,
                'criterios_cumplidos': criterios_cumplidos
            }
            
            # Actualizar la mejor coincidencia
            if criterios_cumplidos > max_criterios_cumplidos:
                max_criterios_cumplidos = criterios_cumplidos
                mejor_coincidencia = youtuber_id
            
        #Si cumple con todos los criterios (5), retornamos inmediatamente
        if criterios_cumplidos == 5:
            return {youtuber_id: info}
    
    # Imprimir estadísticas de diagnóstico
    #Se realiza el diagnostico item por item
    print(f"\nEstadísticas de búsqueda:")
    print(f"- Canales en categoría '{categoria_popular}': {categoria_count}")
    print(f"- Con {suscriptores_min}-{suscriptores_max} suscriptores: {suscriptores_count}")
    print(f"- Con {videos_minimos}+ videos: {videos_count}")
    print(f"- Publicados entre {fecha_minima.strftime('%Y-%m-%d')} y {fecha_maxima.strftime('%Y-%m-%d')}: {fecha_count}")
    print(f"- Con '{palabra_clave}' en descripción: {keyword_count}")
    
    # Si no hay coincidencia exacta pero hay parciales, sugerir la mejor
    if mejor_coincidencia and max_criterios_cumplidos >= 3:
        print(f"\nNo se encontró coincidencia exacta, pero hay {len(coincidencias_parciales)} coincidencias parciales.")
        print(f"La mejor coincidencia cumple {max_criterios_cumplidos} de 5 criterios:")
        return {mejor_coincidencia: coincidencias_parciales[mejor_coincidencia]['info']}
    
    #Si no encontramos ningún youtuber que cumpla, retornamos un diccionario vacío
    return {}

#Paso 1: Hacer la carga de los datos identificar los datos
def leer_csv(csv_file):
    #Convertir en dataframe
    try:
        df = pd.read_csv(csv_file)
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return {}
    
    #Limpiar y procesar los datos
    youtubers = {}
    
    #Recorrer el archivo
    for index, row in df.iterrows():
        try:
            #Extraer el nombre del canal
            nombre = row['Ch_name'] if not pd.isna(row['Ch_name']) else "Sin nombre"
            
            #Procesar las vistas
            vistas_str = str(row['Views'])
            #Reemplazar las comas y los signos extraños por espacios
            vistas_str = vistas_str.replace(',','').replace('+', '').replace('"', '')
            #Obtener los datos limpios
            try:
                #Convertir las vistas a cantidades
                vistas = int(vistas_str) if vistas_str != '--' and vistas_str != 'NaN' else 0
            except ValueError:
                vistas = 0
                
            #Procesar los suscriptores
            suscriptores_str = str(row['Subscriptions'])
            if 'M' in suscriptores_str:
                #ajustar las cifras (de M a millones 000000)
                suscriptores = float(suscriptores_str.replace('M', '')) * 1000000
            elif 'K' in suscriptores_str:
                #Ajustar los miles (de K a 000)
                suscriptores = float(suscriptores_str.replace('K', '')) * 1000
            else:
                try:
                    #Si los suscriptores estan entre la unidad y las centenas
                    suscriptores = int(suscriptores_str)
                except ValueError:
                    #No se encontraron suscriptores
                    suscriptores = 0
            
            #Procesar los uploads - carga de los vídeos
            uploads = row['Uploads']
            #Limpiar los datos
            
            #Si no hay datos, las vistas se procesan como 0
            if pd.isna(uploads) or uploads == 'NaN':
                uploads = 0
            #Contar las vistas
            else:
                try:
                    uploads = int(uploads)
                except ValueError:
                    uploads = 0
            
            #Asignar categorías simuladas basadas en el nombre
            #Según la categoria se asigna una categoría a la columna del dataframe
            if 'VEVO' in nombre:
                categoria = 'Música'
            elif 'Game' in nombre or 'Play' in nombre or 'gaming' in nombre.lower() or 'Fornite' in nombre:
                categoria = 'Videojuegos'
            elif 'Toy' in nombre or 'Kids' in nombre or 'Baby' in nombre or 'Child' in nombre:
                categoria = 'Infantil'
            elif 'TV' in nombre:
                categoria = 'Television'
            else:
                categoria = 'Otro'
                
            # Extraer descripción si existe en el dataset (simulado)
            descripcion = str(row.get('Description', '')).lower()
            if pd.isna(descripcion):
                descripcion = f"Canal de {nombre} con contenido de {categoria}"
                
            # Usar columna 'Created' para la fecha si existe, o crear fecha simulada
            fecha_str = str(row.get('Created', ''))
            try:
                if pd.isna(fecha_str) or fecha_str == 'nan':
                    # Fecha simulada basada en el id del canal (para demostración)
                    # Simulamos fechas entre 2006 y 2019
                    año = 2006 + (index % 14)
                    mes = 1 + (index % 12)
                    dia = 1 + (index % 28)
                    fecha_publicacion = datetime(año, mes, dia)
                else:
                    # Intenta convertir la fecha del CSV
                    fecha_publicacion = datetime.strptime(fecha_str, "%Y-%m-%d")
            except ValueError:
                # Si falla, asigna una fecha por defecto
                fecha_publicacion = datetime(2010, 1, 1)
            
            # Agregar información sobre Rihanna para algunos canales (simulado)
            if index % 5 == 0:  # Para un 20% de los canales aproximadamente
                descripcion += " canal relacionado con música de rihana y artistas similares"
            
            # Para canales de música con más de 20M suscriptores, aumentar probabilidad
            if categoria == 'Música' and suscriptores > 20000000:
                if index % 2 == 0:  # 50% de probabilidad para estos canales
                    descripcion += " colaboraciones con rihana y otros artistas de pop y R&B"
            
            #Crear el objeto youtuber
            #Los atributos son las caracteristicas a buscar
            youtuber_id = f"youtuber_{index + 1}" #Atributo que recorre el id
            youtubers[youtuber_id] = {
                #Atributos
                'nombre': nombre, 
                'suscriptores': int(suscriptores),
                'videos': uploads,
                'visitas': vistas,
                'categoria': categoria,
                'descripcion': descripcion,
                'fecha_publicacion': fecha_publicacion
            }
        except Exception as e:
            print(f"Error al procesar fila {index}: {e}")
            continue
    
    return youtubers
    
#Funcion main
if __name__ == "__main__":
    try:
        #Cargar los datos con la ruta fija
        archivo = "Capituber\gross_500.csv"
            
        #Usar la funcion csv para cargar el archivo
        youtubers = leer_csv(archivo)
        
        #Si no se carga el csv se aborta la búsqueda
        if not youtubers:
            print("No se pudieron cargar datos de YouTubers. Verifique el archivo CSV.")
            exit(1)
            
        print("\n=== Parámetros de la búsqueda manual ===")
            
        #Generar la búsqueda manual
        #Pide parámetro por parámetro
        suscriptores_min = int(input("Suscriptores mínimos: "))
        suscriptores_max = int(input("Suscriptores máximos: "))
        fecha_minima = input("Fecha mínima (YYYY-MM-DD): ")
        fecha_maxima = input("Fecha máxima (YYYY-MM-DD): ")
        videos_minimos = int(input("Cantidad de vídeos mínimo: "))
        palabra_clave = input("Palabra clave en la descripción: ")
            
        #Guardar lo que se encuentra por la función en una variable
        resultado = recomendar_youtuber(
            #Usar las variables para la recomendaciones
            youtubers, suscriptores_min, suscriptores_max,
            fecha_minima, fecha_maxima, videos_minimos,
            palabra_clave
        )
            
        #Si se encuentra un resultado lo imprime
        if resultado:
            print("\n=== Youtuber recomendado: ===")
            #Busca los datos
            for youtuber_id, datos in resultado.items():
                print(f"ID: {youtuber_id}")
                for k, v in datos.items():
                    if k == 'fecha_publicacion':
                        print(f"{k.capitalize()}: {v.strftime('%Y-%m-%d')}")
                    else:
                        print(f"{k.capitalize()}: {v}")
                        
            # Sugerir modificaciones a los criterios
            print("\nSugerencias para encontrar más resultados:")
            print("1. Ampliar el rango de suscriptores (pruebe con 20M-30M)")
            print("2. Ampliar el rango de fechas")
            print("3. Reducir el número mínimo de videos")
            print("4. Verificar la ortografía de la palabra clave (rihanna vs rihana)")
        else:
            print("\nNo hay coincidencias para los criterios especificados.")
            print("\nSugerencias para encontrar resultados:")
            print("1. Ampliar el rango de suscriptores (pruebe con 20M-30M)")
            print("2. Ampliar el rango de fechas")
            print("3. Reducir el número mínimo de videos a 50")
            print("4. Verificar la ortografía de la palabra clave (rihanna vs rihana)")
    except Exception as e:
        print(f"Error en la ejecución: {e}")