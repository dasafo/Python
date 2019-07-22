import re

cadena="vamos a aprender expresiones regulares en Python.Python es un lenguaje de sintaxis sencilla"

#para que nos busque si existe una cadena de caracteres
print(re.search("aprender", cadena)) 

#Lo mismo pero ahora que nos avise si no se encuentra nada(None)
textBuscar="regulares"

if( re.search(textBuscar,cadena)) is not None:

    print("He encontrado 1 texto")

else:

    print("No he encontrado nada")


#Para que nos muestre la posicion del primer caracter de la palabra buscada('regulares')
textoEncontrado=re.search(textBuscar, cadena)

print(textoEncontrado.start()) #muestra la primera posicion desde el principio
print(textoEncontrado.end()) #muestra el primero encontrado desde el final
print(textoEncontrado.span()) #muestra la posicion inicial y final de la palabra buscada

#Para que nos meta el texto a buscar en un array(findall) y nos muestre las veces que aparece(len)
textBuscar2="Python"
print(len(re.findall(textBuscar2,cadena)))