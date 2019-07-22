import sqlite3

miConexion=sqlite3.connect("GestionProductos")

miCursor=miConexion.cursor()
#Leer tablas
miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='Confección'")

pruductos=miCursor.fetchall()

print(pruductos)

miConexion.commit()

miConexion.close()