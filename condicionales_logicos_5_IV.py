print("Programa becas ano 2020")

distancia_escuela=int(input("Intriduce la distancia hasta la escuela en Km: "))
print(distancia_escuela)

numero_hermanos=int(input("N de hermanos: "))
print(numero_hermanos)

salario_familiar=int(input("Salario familiar: "))
print(salario_familiar)

if distancia_escuela>40 and numero_hermanos>2 or salario_familiar<=20000:
	print("Tienes derecho a beca")
else: 
	print("No tienes derecho a beca")


