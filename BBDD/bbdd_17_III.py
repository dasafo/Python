import sqlite3

miConexion=sqlite3.connect("BBDD/GestionProductos")


miCursor=miConexion.cursor()

miCursor.execute("INSERT INTO PRODUCTOS VALUES ('AR05', 'Tren', 14,'Jugetería')")


miConexion.commit()

miConexion.close()