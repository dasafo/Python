contador=0
miemail=input("Introcude el correo email: ")

for i in miemail:

	if(i=="@" or i=="."):

		contador=contador+1

if contador==2:
	print("Email correcto")
else:
	print("Correo incorrecto")