#Importar sqlite
import sqlite3 as sql

'''
Vamos a crear una base de datos de streamers de twitch
'''

#Crear la base de datos 
def crearDB():
    #Crear el conector para la base de datos
    con = sql.connect("streamers.db")
    con.commit()
    con.close()
    

'''

'''

def crearTabla():
    #Nombres y columnas de las tablas
    con = sql.connect("streamers.db")
    #Crear el cursor
    cursor = con.cursor()
    cursor.execute(
        #Mandar un docstring
        """CREATE TABLE streamers (
            name text,
            followers integer,
            subs integer
            )"""
    )
    #Realizar el commit
    con.commit()
    con.close()


#Insertar una fila
def insertarFila(nombre, followers, subs):
    #Nombres y columnas de las tablas
    con = sql.connect("streamers.db")
    #Crear el cursor
    cursor = con.cursor()
    query = f"INSERT INTO streamers VALUES('{nombre}', {followers}, {subs})"
    cursor.execute(query)
    #Realizar el commit
    con.commit()
    con.close()

#Leer la fila
def readFila():
    #Nombres y columnas de las tablas
    con = sql.connect("streamers.db")
    #Crear el cursor
    cursor = con.cursor()
    query = f"SELECT * FROM streamers"
    cursor.execute(query)
    datos = cursor.fetchall()
    #Realizar el commit
    con.commit()
    con.close()
    print(datos)
    
#Insertar varias filas en una instancia
def insertRows(streamerList):
    #Nombres y columnas de las tablas
    con = sql.connect("streamers.db")
    #Crear el cursor
    cursor = con.cursor()
    #Vamos a pasar 3 valores para cada fila
    #Nombre, followers y subs
    query = f"INSERT INTO streamers VALUES(?, ?, ?)"
    #Ejecutar muchos queries
    cursor.executemany(query, streamerList)
    con.commit()
    con.close()
    
    
#Ordenar las filas
#Field -> Campo por el que se quiere ordenar
def orderRows(field):
    #Nombres y columnas de las tablas
    con = sql.connect("streamers.db")
    #Crear el cursor
    cursor = con.cursor()
    query = f"SELECT * FROM streamers ORDER BY {field}"
    cursor.execute(query)
    datos = cursor.fetchall()
    #Realizar el commit
    con.commit()
    con.close()
    print(datos)
    
def busquedas():
    #Nombres y columnas de las tablas
    con = sql.connect("streamers.db")
    #Crear el cursor
    cursor = con.cursor()
    query = f"SELECT * FROM streamers WHERE  name = 'Alex'"
    cursor.execute(query)
    datos = cursor.fetchall()
    #Realizar el commit
    con.commit()
    con.close()
    print(datos)
    
    
#Usar condicionales
def condicionales():
    #Nombres y columnas de las tablas
    con = sql.connect("streamers.db")
    #Crear el cursor
    cursor = con.cursor()
    query = f"SELECT * FROM streamers WHERE  subs > 6000"
    cursor.execute(query)
    datos = cursor.fetchall()
    #Realizar el commit
    con.commit()
    con.close()
    print(datos)
    
#Actualizar filas
def updateFilas():
    #Nombres y columnas de las tablas
    con = sql.connect("streamers.db")
    #Crear el cursor
    cursor = con.cursor()
    #ordenar por suscriptores de forma descendiente
    query = f"UPDATE streamers SET followers=120000000 WHERE name like 'ElXokas'"
    #Ejecutar el query
    cursor.execute(query)
    datos = cursor.fetchall()
    #Realizar el commit
    con.commit()
    con.close()
    
    
#Crear el entry point
if __name__ == "__main__":
    #crearDB()
    #crearTabla()
    #insertarFila("Alex", 200000, 1000000)
    #readFila()
    streamers = [
        ("ElXokas", 1000000, 9500),
        ("Cristinini", 30000000, 5500),
        ("Auronplay", 8000000, 20000)
    ]
    #insertRows(streamers)
    #orderRows("subs")
    #condicionales()
    updateFilas()