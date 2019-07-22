import sqlite3

#Las mayúsculas son para decir que estmaos introduciendo otro lenguaje(SQL, PHP,..)
#A partir del tercer paso vamos comentando porque hay que ir quitando el paso anteior para ir creando el nuevo


#Primero cremos la conexion a la base de datos
miConexion=sqlite3.connect("BBDD/PrimeraBase")

#Segundo creamos el cursor/puntero
miCursor=miConexion.cursor()

#Tercero ejecutamos sqlite y creamos tabla
miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

#Insertamos un registro en la base de datos
#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALÓN', 15, 'deportes')")


#Ahora insertamos un lote de registros
# variosProductos=[
		
# 		("Camisteas", 10, "Deportes"),
# 		("Jarrón", 90, "Cerámica"),
# 		("Camión", 20, "Juguetería")

# ]

#aplicamos executemany para adjuntar el lote de variosProductos
# miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)


#Ejecutamos y leemos el lote de registros en consola
#miCursor.execute("SELECT * FROM PRODUCTOS")

#variosProductos=miCursor.fetchall()

#for producto in variosProductos:

#	print("Nombre artículo: ", producto[0], " Sección: ", producto[2])



miConexion.commit()

#cerramos la conexion
miConexion.close()