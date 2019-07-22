
def devuelve_ciudades(*ciudades): #con * le indicamos que recibira argumentos indefinidos

	for elemento in ciudades:
		for subElemento in elemento:

			yield subElemento

ciudades_devueltas=devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))


#Ahora utilizamos el 'yield from' para hacer lo mismo pero más simplificado

def devuelve_ciudades2(*ciudades2): #con * le indicamos que recibira argumentos indefinidos

	for elemento2 in ciudades2:
	
			yield from elemento2

ciudades_devueltas2=devuelve_ciudades2("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(ciudades_devueltas2))

print(next(ciudades_devueltas2))

import sys
print(sys.version)

