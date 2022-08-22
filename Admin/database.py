import sqlite3 as sql

def crearBaseDatos(conn):
    cursor= conn.cursor()
    try:
        cursor.execute("""
        CREATE TABLE "Usuarios" (
	    "ID"	INTEGER NOT NULL UNIQUE,
	    "Nombre"	TEXT NOT NULL UNIQUE,
	    PRIMARY KEY("ID" AUTOINCREMENT)
        );
        """)
        conn.commit()
        conn.close()    
        return 'Database created'
    except sql.Error as e:
        return e

def insertarUsuario(conn, Nombre):
    cursor = conn.cursor()
    try:
        cursor.execute(f"INSERT INTO Usuarios (Nombre) VALUES ('{Nombre}');")
        conn.commit()
        conn.close()
        return ("Usuario añadido: ", Nombre)
    except sql.Error as e:
        return ("Error, llame al Administrador\n", e)

def leerUsuario(conn):
    cursor = conn.cursor()
    try: 
        cursor.execute('SELECT * FROM Usuarios')
        datos = cursor.fetchall()
        conn.commit()
        conn.close()
        print(datos)
        return datos 
    except sql.Error as e:
        return (e)


if __name__=='__main__':
    conn = sql.connect('Usuarios.db')
    leerUsuario(conn)
