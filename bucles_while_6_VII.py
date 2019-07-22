import math

print("Programa de cálculo de raiz cuadrada")
numero=int(input("Introduce un numero ostias: "))

intentos=0

while numero<0:
	print("No se puede hallar la raiz de un numero negrativo")

	if intentos==2:
		print("demasiados intentos bye bye")
		break;

	numero=int(input("Introduce un numero ostias: "))
	if numero<0:
		intentos=intentos+1

if intentos<2:
	solucion=math.sqrt(numero)
	print("La raiz cuadrada de " +str(numero) + " es " + str(solucion))

import sys
print(sys.version)