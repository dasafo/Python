edad=-7

if 0<edad<100:
	print("Edad correcta")
else:
	print("Edad incorrecta")


salario_presidente=int(input("Introduce salario presidente "))
print("Salario presidente: " + str(salario_presidente) )

salario_jefe_area=int(input("Introduce salario jefe de area "))
print("Salario jefe de area: " + str(salario_jefe_area) )

salario_administrativo=int(input("Introduce salario administraitvo "))
print("Salario administrativo: " + str(salario_administrativo) )

if salario_administrativo<salario_jefe_area<salario_presidente:
	print("Algo falla, teneis jefe")
else:
	print("Todo All Right")	
