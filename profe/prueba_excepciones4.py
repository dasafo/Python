import math

def calculaRaiz(num1):

	if num1<0:
		raise ValueError ("Número no puede ser negativo")


	else:
		return math.sqrt(num1)

op1=(int(input("Introduce un número: ")))

try:

	print(calculaRaiz(op1))
	
except ValueError as ErroNegativo:

	print(ErroNegativo)

print("Programa terminado")