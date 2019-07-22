class Persona():

	def __init__(self, nombre, edad, lugar_residencia):

		self.nombre=nombre
		self.edad=edad
		self.lugar_residencia=lugar_residencia

	def descripcion(self):

		print("Nombre: ", self.nombre, "Edad: ", self.edad, "Residencia: ", self.lugar_residencia)


class Empleado(Persona):

	def __init__(self, salario, antigüedad, nombre_empleado, edad_empleado, residencia_empleado):

		#Llamamos ahora al constructor padre __init__ con super(). les podemos cambiar el nombre, siempre que lo declaremos antes dentro de esta clase Empleado, el programa usará los métodos de Persona igualmente pero ahora con otro nombre dado aqui.

		super().__init__(nombre_empleado, edad_empleado, residencia_empleado) 
		
		self.salario=salario
		self.antigüedad=antigüedad

	def descripcion(self):

		super().descripcion()

		print("Salario: ", self.salario,"antigüedad: ", self.antigüedad)


Manuel=Empleado(1500, 15, "Manuel", 55, "Colombia")
Manuel.descripcion()

#Vamos a comprobar la clase de Manuel con isinstance() (devuelve True o False)
print(isinstance(Manuel, Empleado))
