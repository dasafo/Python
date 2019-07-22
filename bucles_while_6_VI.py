edad=int(input("Introduce tu edad: "))

while edad<5 or edad>100:
	print("Has introducido una edad incorrecta, vuelve a intentarlo")
	edad=int(input("Introduce tu edad: "))

print("Gracias por nada")
print("Tienes " + str(edad))
