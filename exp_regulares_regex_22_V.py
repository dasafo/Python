import re

nombre1="JorGe Pla"

nombre2="David Salas"

nombre3="Jara Latorre"

cadena1="Lara Latorre"

cadena2="54546545"

cadena3="a456666"


if re.match("Jorge", nombre1, re.IGNORECASE): #ignorecase para que ignore las mayusculas/minusculas

    print("Hemos encontraod el nombre")

else:

    print("no lo hemos encontrado")



if re.match(".ara", nombre1, re.IGNORECASE): #ignorecase para que ignore las mayusculas/minusculas

    print("Hemos encontraod el nombre")

else:

    print("no lo hemos encontrado")


if re.match("\d", cadena2): 

    print("Hemos encontraod el numero")

else:

    print("no lo hemos encontrado")


if re.search("Pla", nombre1): #ignorecase para que ignore las mayusculas/minusculas

    print("Hemos encontraod el nombre")

else:

    print("no lo hemos encontrado")