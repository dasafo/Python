# -*- coding: utf-8 -*-

#Copiamos el POO creado anteriormente eliminando las instancias solo
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
			return "La furgo está cargada"
		else:
			return "La furgo no está cargada"


class Moto(Vehiculos):
	hcaballito=""
	def caballito(self):
		self.hcaballito="Voy haciendo el cabra"

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


