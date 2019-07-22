# -*- coding: utf-8 -*-

#Creamos objeto/instancia
nombreUsuario=input("Introduce tu nombre de usuario: ")

#usamos metodos que tiene Python para los strings
print("El nombre es: ", nombreUsuario.upper()) #Pone nombre en mayusculas
print("El nombre es: ", nombreUsuario.lower()) #Pone el nobre en minusculas

print("El nombre es: ", nombreUsuario.capitalize()) #Primera letra en mayúscula





edad=input("Introduce la edad: ")
print(edad.isdigit()) #devuelve True o False dependiendo si hemos introducido un digito o no

while(edad.isdigit()==False):

	print("Introduce un valor numérico")
	edad=input("Introduce la edad: ")

if(int(edad)<18): #pasamos a int ya que el numero introducido Python lo lee como string
	print("No puede pasar")
else:
	print("Puede pasar")