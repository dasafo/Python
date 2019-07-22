print("Verificcacion de acceso")

#El IF actua como un solo bloque con el ELIF
edad_usuario=int(input("Introduce tu edad, por favore: "))

if edad_usuario<18:
	print("No pasas chaval")
elif edad_usuario>100:
	print("Edad Incorrecta espabilao")
else:
	print("Pasa pero con cuidao chaval")


#El IF actua como varios bloques
nota_alumno=int(input("Introudce tu nota: "))

if nota_alumno<5:
	print("Insuficiente")
if nota_alumno<6:
	print("Bien")
if nota_alumno<7:
	print("Notable")
else:
	print("Sobresaliente campeon")

print("Mierda terminada")


