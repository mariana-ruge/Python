# Recomendador de YouTubers

Este proyecto es una herramienta en Python diseñada para recomendar un canal de YouTube (YouTuber) que cumpla con ciertos criterios personalizados, como número de suscriptores, cantidad de videos subidos, palabra clave en la descripción, entre otros.

## Clonación del Proyecto

Puedes clonar este repositorio en tu entorno local usando el siguiente comando:

```bash
git clone https://github.com/mariana-ruge/Python/tree/main
cd Capituber
```

Asegúrese de tener instalado Python 3.7 o superior, y las dependencias necesarias:

```bash
pip install pandas
```

## Estructura de Archivos

```
Capituber/
├── gross_500.csv           # Archivo CSV con los datos de entrada
├── recomendador.py         # Script principal con la lógica del recomendador
└── README.md               # Este archivo
```

## Ejecución

Para ejecutar el script principal:

```bash
python capituber.py
```

El programa solicitará que ingreses los parámetros de búsqueda por consola:
* Rango de suscriptores
* Rango de fechas de creación del canal
* Mínimo de videos subidos
* Palabra clave en la descripción del canal

## Algoritmo y Lógica del Recomendador

1. **Carga de Datos:** Se lee un archivo CSV con información de los canales de YouTube. Se procesan campos como:
   * Nombre del canal
   * Vistas, suscriptores, número de videos subidos
   * Descripción del canal
   * Fecha de creación del canal
   * Categoría (asignada con reglas heurísticas)

2. **Identificación de Categoría Popular:** Se calcula cuál es la categoría con mayor cantidad de visitas totales. Solo se consideran canales dentro de esta categoría para la recomendación.

3. **Filtrado por Criterios:** Para cada canal en la categoría popular:
   * Debe tener suscriptores dentro del rango especificado.
   * Debe tener al menos la cantidad de videos indicada.
   * La fecha de creación debe estar dentro del rango.
   * La descripción debe contener la palabra clave, sin distinguir mayúsculas/minúsculas.

4. **Recomendación:**
   * Si un canal cumple todos los criterios, se retorna inmediatamente.
   * Si ninguno cumple con todo, se muestra la mejor coincidencia parcial (con al menos 3 de los 5 criterios).

5. **Diagnóstico:** Se imprimen estadísticas de cuántos canales cumplen con cada criterio, y se sugieren formas de relajar los filtros para obtener más resultados.

## Ejemplo de Uso

```
=== Parámetros de la búsqueda manual ===
Suscriptores mínimos: 20000000
Suscriptores máximos: 50000000
Fecha mínima (YYYY-MM-DD): 2007-01-01
Fecha máxima (YYYY-MM-DD): 2018-01-01
Cantidad de vídeos mínimo: 50
Palabra clave en la descripción: musica

Categoría más popular: Música

Estadísticas de búsqueda:
- Canales en categoría 'Música': 127
- Con 20000000-50000000 suscriptores: 45
- Con 50+ videos: 89
- Publicados entre 2007-01-01 y 2018-01-01: 108
- Con 'musica' en descripción: 63

=== Youtuber recomendado: ===
ID: youtuber_87
Nombre: JustinBieberVEVO
Suscriptores: 28453921
Videos: 96
Visitas: 19874563210
Categoria: Música
Descripcion: canal relacionado con musica pop y R&B
Fecha_publicacion: 2010-04-15
```

## Recomendaciones para una Búsqueda Exitosa

Si no se encuentran coincidencias exactas con los criterios específicos, pruebe:

1. **Ampliar el rango de suscriptores** (por ejemplo, de 20M a 50M)
2. **Extender el período de fechas** (cubrir más años)
3. **Reducir el requisito mínimo de videos**
4. **Usar palabras clave más comunes** en la categoría de interés

## Contribuciones

Las contribuciones son bienvenidas. Por favor, siéntase libre de bifurcar el repositorio, realizar mejoras y enviar solicitudes de extracción.
