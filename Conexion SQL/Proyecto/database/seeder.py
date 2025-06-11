import sqlite3 as sql

#Ruta a la base de datos
DB_PATH = r'C:\Users\maria\OneDrive\Escritorio\Códigos\Python\Conexion SQL\streamers.db'

#Crear la base de datos y la tabla
def createDB():
    #Crear la conexión
    conn = sql.connect(DB_PATH)
    #Crear el cursor
    cursor = conn.cursor()
    #Ejecutar los queries
    cursor.execute(
        """
        CREATE TABLE streamers_actualizado(
            name text,
            subs integer,
            followers integer
        )
        """
    )
    conn.commit()
    conn.close()
    

#Añadir valores a la tabla
def addValues():
    #Crear la conexión
    conn = sql.connect(DB_PATH)
    #Crear el cursor
    cursor = conn.cursor()
    #Lista con los Streamers
    data = [
        ("alexcapo", 100000,  200000),
        ("ibai", 250000, 70000000),
        ("auronplay", 200000, 5000000),
        ("cristinini", 5500, 3000000)
    ]
    cursor.executemany("""INSERT INTO streamers_actualizado VALUES (?, ?, ?)""", data)
    conn.commit()
    conn.close()
    

def borrar_tabla():
    DB_PATH_AT = r'C:\Users\maria\OneDrive\Escritorio\Códigos\Python\Conexion SQL\streamers.db'

    conn = sql.connect(DB_PATH_AT)
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS streamers")  # 👈 elimina la tabla antigua
    conn.commit()
    conn.close()


#Crear el Entry Point
if __name__ == "__main__":
    #Crear la tabla
    #createDB()
    #Añadir los valores
    #addValues()
    borrar_tabla()
    
