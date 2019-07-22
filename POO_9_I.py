# -*- coding: utf-8 -*-

class Coche():

    #Ponemos un contructor que le de estado inicial(porpiedades) a los objetos de esta clase
	def __init__(self):

	#Propiedades
		self.largoChasis=250
		self.anchoChasis=120
		self.__ruedas=4 #Encapsulamos la propiedad con __, as� no es accesible desde fuera de la clase.
		self.enmarcha=False #Tambien se puede encapsular. solo hará caso a los métodos(dentro de class).

	#Comportamiento
	#Definimos 3 métodos (defs)
	def arrancar(self,arrancamos):
		self.enmarcha=arrancamos

		if(self.enmarcha):
			chequeo=self.__chequeo_interno()

		if(self.enmarcha and chequeo):
			return "El coche está en marcha"

		elif(self.enmarcha and chequeo==False):
			return "Algo ha ido mal en el chequeo"

		else:
			return "El coche está quieto"
		
	def estado(self):
		print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.anchoChasis, 
			" y un largo de ", self.anchoChasis)
		

	def __chequeo_interno(self):
		print("...realizando chequeo interno...")

		self.gasolina="OK"
		self.aceite="OK"
		self.puertas="CERRADAS"

		if(self.gasolina=="OK" and self.aceite=="OK" and self.puertas=="CERRADAS"):
				
				return True

		else:

				return False



print("-----Creamos el Primer objeto------")
#Ahora creamos el objeto que pertenece a la clase 'coche'
miCoche=Coche()
#Ahora damos a 'miCoche' el valor de 'arrancar'(True)
print(miCoche.arrancar(True))
#Comprobamos que está en 'arrancar' con la función 'estado'
miCoche.estado()
#Comprobamos que tenemos encapsulado el método chequeo interno, nopudiendo acceder a el(sale error).
#print(miCoche.__chequeo_interno())

print("-----A continuación creamos el segundo objeto------")

miCoche2=Coche()
print(miCoche2.arrancar(False))
#cambiamos las ruedas(vemos que no nos deja gracias a la definición del contructor de arriba. Encapsulamiento)
miCoche2.__ruedas=2 
miCoche2.estado()