import pickle

class Persona:

	def __init__(self, nombre, genero, edad):
		self.nombre=nombre
		self.genero=genero
		self.edad=edad
		print("Se ha creado una persona nueva con el nombre de ", self.nombre)
		
	#convierte en una cadena de texto la info de un objeto
	def __str__(self):
		return "{} {} {}".format(self.nombre, self.genero, self.edad)

class listaPersonas:

	personas=[]

	def __init__(self):

		listaDePersonas=open("ficheroExterno", "ab+")
		listaDePersonas.seek(0)

		try:
			self.personas=pickle.load(listaDePersonas)
			print("Se cargaron {} personas del fichero exerno".format(len(self.personas)))

		except:
			print("El fichero está vacio")

		finally:
			listaDePersonas.close()
			del(listaDePersonas)


	def agregarPersonas(self, p):
		self.personas.append(p)
		self.guardarPersonasEnFicheroExterno()

	def mostrarPersonas(self):
		for p in self.personas:
			print(p)

	def guardarPersonasEnFicheroExterno(self):
		listaDePersonas=open("ficheroExterno", "wb")
		pickle.dump(self.personas, listaDePersonas)
		listaDePersonas.close()
		del(listaDePersonas)

	def mostrasInfoFicheroExterno(self):
		print("La informacción del fichero externo es la siguiente: ")
		for p in self.personas:
			print(p)

miLista=listaPersonas()
persona=Persona("David", "Masculino", 33)
miLista.agregarPersonas(persona)
miLista.mostrasInfoFicheroExterno()

#p=persona("Sandra", "Femenino", 29)
#miLista.agregarPersonas(p)
#p=persona("Antonio", "MAssculino", 57)
#miLista.agregarPersonas(p)
#p=persona("Ana", "Femenino", 13)
#miLista.agregarPersonas(p)

#miLista.mostrarPersonas()