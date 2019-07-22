#importamos la biblioteca 'io' de python para trabajar con flujo de datos, y su metodo 'open'
from io import open

archivo_texto=open("archivo.txt", "w") #'r' modo lectura

frase="Estupendo día para morir \n en esta ciudad"

archivo_texto.write(frase)

archivo_texto.close()


#Ahora lo leemos y decimos que nos diga lo que pone en ese archivo

archivo_texto=open("archivo.txt", "r")

texto=archivo_texto.read()

archivo_texto.close()

print(texto)

#Ahora almacenamos en una lista cada elemento del contenido del texto

archivo_texto=open("archivo.txt", "r")

lineas_text=archivo_texto.readlines() #readlines() nos lee el archivo linea a linea y lo almacena en un array, cada linea una posicion en el array.

archivo_texto.close()

print(lineas_text[0]) #Podemos elegir que nos diga el elemento de la lista que queramos [..]


#Ahora agregamos información al archivo

archivo_texto=open("archivo.txt", "a") #añadimos usando 'a' de append

archivo_texto.write("\n auqnue no es una buena idea")

archivo_texto.close()