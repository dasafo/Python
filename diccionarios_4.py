#dicionarios con Clave:Valor
midiccionario={"Alemania":"Berlin", "Francia":"Paris", "UK":"Londres", "Espana":"Madrid"}
print(midiccionario["Francia"])

midiccionario["Italia"]="Lisboa"
print(midiccionario)

#Corregir un valor de una clave,sobrescribe el nuevo valor
midiccionario["Italia"]="Roma"
print(midiccionario)

#Elimnar elementos
del midiccionario["UK"]
print(midiccionario)


#Diccionario en cuanto a tipos
midiccionario2={"Alemania":"Berlin", 23:"Jordan", "Mosqueteros":3}
print(midiccionario2)


mitupla=("Espana", "Francia", "UK", "Alemania")
midiccionario3={mitupla[0]:"Madrid", mitupla[1]:"Paris", mitupla[2]:"Londres", mitupla[3]:"Berlin"}
print(midiccionario3)
print(midiccionario3["Francia"])

midiccionario4={23:"Jordan", "Nombre":"Michel", "Equipo":"Chicago", "anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}
print(midiccionario4["Equipo"])
print(midiccionario4["anillos"])

#Todas las claves de un dcionario
print(midiccionario4.keys())

#Todos los valores de las clvaves
print(midiccionario4.values())

#Longitud de los valores del diccionario
print(len(midiccionario4))