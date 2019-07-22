mitupla=("Juan",13,45,78,45)

print(mitupla[2])

#Convertir una tupla en una lista

milista=list(mitupla)
print(milista)

#Volvemos a convertir en tupla
mitupla=tuple(milista)
print(mitupla)

#Confirmar si existe un dato
print("Juan" in milista)

#Cautnos elementos se encuentran dentro de una tupla
print(mitupla.count(45))

#Numero de elementos en la tupla
print(len(mitupla))

#Tupla con un unico elemento poniendo una coma

mitupla2=("Juan",)
print(len(mitupla2))

#podemos poner tuplas sin parentesis tambien

mitupla3=45,"David",56.67
print(mitupla3)


#Desempaquetado de tuplas
mitupla4=("Juan", 13, 1, 1995)
nombre, dia, mes, agno = mitupla4
print(nombre)
print(dia)
print(agno)
print(mes)

