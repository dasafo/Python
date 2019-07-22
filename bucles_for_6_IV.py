valido=False

email=input("Introduce email: ")

for i in range(len(email)):  #range() crea una lista, en este caso con las posiciones que dé len()
	if email[i]=="@":

		valido=True

if valido:

	print("Email correcto")

else:

	print("Email incorrecto")

