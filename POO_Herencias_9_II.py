# -*- coding: utf-8 -*-


class Vehiculos():

	def __init__(self, marca, modelo):

		self.marca=marca
		self.modelo=modelo
		self.enmarcha=False
		self.acelera=False
		self.frena=False

	def arrancar(self):
		self.enmarcha=True

	def acelerar(self):
		self.acelera=True

	def frenar(self):
		self.frena=True

	def estado(self):
		print("Marca: ", self.marca, "\nModelo: ", self.modelo,
			self.enmarcha, " \nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)


class Furgoneta(Vehiculos):

	def carga(self, cargar):
		self.cargado=cargar
		if(self.cargado):
			return "La furgo está cargada\n"
		else:
			return "La furgo no está cargada\n"


class Moto(Vehiculos):
	hcaballito=""
	def caballito(self):
		self.hcaballito="Voy haciendo el cabra\n"

	#El estado hijo sobreescribe al padre siempre
	def estado(self):
		print("Marca: ", self.marca, "\nModelo: ", self.modelo,
			self.enmarcha, " \nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\n", self.hcaballito)


class VElectricos(Vehiculos):
	def __init__(self, marca, modelo):

		super().__init__(marca, modelo) #Ver Herencias_2
		self.autonomia=100

	def cargarEnergia(self):
		self.cargando=True



miMoto=Moto("Honda", "CBR")
miMoto.caballito()
miMoto.estado()

miFurgoneta=Furgoneta("Renault", "Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True)) #Lo metemos dentro del print porque el estado de furgoneta no saca un print, cosa que si pasa con la moto, y por eso ahí no hace falta

#Caundo hay herencia múltiple se le da preferencia a la primera que se pone como herencia, en este caso VElectricos.
class BicicletaElectrica(VElectricos, Vehiculos):
	pass

miBici=BicicletaElectrica("Orbea","HPI") #Hereda el __init__ de VElectricos

