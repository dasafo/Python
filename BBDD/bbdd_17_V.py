import sqlite3

miConexion=sqlite3.connect("GestionProductos")

miCursor=miConexion.cursor()
#PAra actualizar registros
miCursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO='pelota'")



miConexion.commit()

miConexion.close()