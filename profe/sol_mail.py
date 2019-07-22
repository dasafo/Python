mailUsuario=input("introduce dirección email: ")

arroba=mailUsuario.count('@')

if(arroba!=1 or mailUsuario.rfind('@')==len(mailUsuario)-1 or mailUsuario.find('@')==0):
	print("Mail incorrecto")	
else:
	print("Email correcto")