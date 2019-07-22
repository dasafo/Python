class Empleado:

	def __init__(self, nombre, cargo, salario):

		self.nombre=nombre

		self.cargo=cargo

		self.salario=salario

	def __str__(self):

		return "{} que trabaja como {} tiene un salario de {} €".format(self.nombre, self.cargo, self.salario)


lista_empleados=[

Empleado("Juan", "Director", 75000),

Empleado("Ana", "Presidenta", 85000),

Empleado("Antonio", "Administrativo", 25000),

Empleado("Sara", "Secretaria", 27000),

Empleado("Mario", "Pringado", 21000),

]

salarios_altos=filter(lambda empleado:empleado.salario>50000, lista_empleados)

for empleado_salario in salarios_altos:

	print(empleado_salario)