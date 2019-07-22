class Coche():

	def desplazamiento(self):
		print("Me desplazo a cuatro ruedas")

class Moto():

	def desplazamiento(self):
		print("Me desplazo a dos ruedas")


class Camion():

	def desplazamiento(self):
		print("Me desplazo a seis ruedas")

#Comenzamos el polimorfismo:

def desplazamientoVehiculo(vehiculo):
	vehiculo.desplazamiento()

miVehiculo=Camion()

desplazamientoVehiculo(miVehiculo)