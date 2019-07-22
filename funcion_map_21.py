class Empleado:
    
	def __init__(self, nombre, cargo, salario):

		self.nombre=nombre

		self.cargo=cargo

		self.salario=salario

	def __str__(self):

		return "{} que trabaja como {} tiene un salario de {} €".format(self.nombre, self.cargo, self.salario)


lista_empleados=[

Empleado("Juan", "Director", 6500),

Empleado("Ana", "Presidenta", 5000),

Empleado("Antonio", "Administrativo", 2000),

Empleado("Sara", "Secretaria", 1500),

Empleado("Mario", "Pringado", 1000),

]

def calculo_comision(Empleado):

    if(Empleado.salario<=3000):

        Empleado.salario=Empleado.salario*1.03

    return Empleado

listaEmpleadosComision=map(calculo_comision, lista_empleados)

for Empleado in listaEmpleadosComision:
    print(Empleado)
