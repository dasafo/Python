import sqlite3

miConexion=sqlite3.connect("GestionProductos")

miCursor=miConexion.cursor()
#PAra borrar registros por tema que queramos(ID, precio, nombre de artículo,...)
miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=5")



miConexion.commit()

miConexion.close()