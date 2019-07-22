milista=["Maria","David", "Paula",True, 76.7]

#Aadir un dato al final de la lista
milista.append("Sandra")

#Elegir posicion donde aadir dato y el dato
milista.insert(2,"Pepe")

#Anidar una lista dentro de otra
milista.extend(["Diego","Pepeita"])

#Eliminar un elemento
milista.remove("David")

#Eliminar el ultimo elemento de una lista
milista.pop()


print(milista[-2]) #empieza a contar desde el final sin el 0
print(milista[2])
print(milista[:3]) #la posicion 3 no sale
print(milista[1:3])
print(milista[2:]) #Saca a partir de la posicion 2 (inlcuida) hasta el final
print(milista[:])

#Para saber que posicion ocupa un dato(siempre nos muestra el indice del primero, si ese valor/string esta repetido)
print(milista.index("Sandra"))

#Comprobar si un dato se encuentra en una lista (TRue/False)
print("pepe" in milista)


milista2=["Sandra",57]

#Sumar y multiplicar listas
milista3=milista+milista2

print(milista3) * 2