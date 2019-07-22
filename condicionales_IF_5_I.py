print("Programa de notas de alumnos")

#introduccion de datos por teclado
nota_alumno=input("Introduzca la nota del alumno: ")

def evaluacion(nota):
	valoracion="Aprobado"
	if nota<5:
		valoracion="Suspenso"
	return valoracion

# print(evaluacion(4))

#Imprimios el resultado en entero int(aunque ya no hace falta)
print(evaluacion(int(nota_alumno)))