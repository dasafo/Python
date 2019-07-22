# -*- coding: utf-8 -*-
for letra in "Python":

#Saltamos la letra h
	if letra=="h":
		continue

	print("Viendo la letra: " + letra)



nombre="Píldoras Informáticas"
contador=0
for i in nombre:
#Para saber cuantas letras, no espacios en blanco
	if i==" ":
		continue
	contador+=1
	
print(contador)