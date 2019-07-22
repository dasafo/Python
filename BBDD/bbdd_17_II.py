import sqlite3

miConexion=sqlite3.connect("BBDD/GestionProductos")


miCursor=miConexion.cursor()

#Campo clave(PRIMARY KEY) #Con UNIQUE no se repite información en el nombre articulo(igual que en ID). Usamos ''' para ponerlo en diferentes reglones
miCursor.execute('''
	CREATE TABLE PRODUCTOS (
	ID INTEGER PRIMARY KEY AUTOINCREMENT, 
	NOMBRE_ARTICULO VARCHAR(50) UNIQUE, 
	PRECIO INTEGER,
	SECCION VARCHAR(20))
''')

productos=[
		
	("pelota", 20, "Juguetería"),
	("pantalón", 15, "Confección"),
	("destornillador", 25, "Ferretería"),
	("jarrón", 45, "Cerámica"),
	("pantalones", 35, "Confección")
]


miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?,?)", productos)


miConexion.commit()

miConexion.close()