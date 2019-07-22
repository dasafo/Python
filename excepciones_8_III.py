def evaluaEdad(edad):

	if edad<0:
		raise TypeError("Edad negativa!") #Podemos personalizar el mensaje de error
		
	if edad<20:
		return "eres muy joven pipiolo"
	elif edad<40:
		return "eres viejoven"
	elif edad<65:
		return "eres viejo"
	elif edad<100:
		return "Hueles a tierra"

print(evaluaEdad(18))