from io import open

archivo_texto=open("archivo.txt", "r+") # r+ es de lectura y escritura
print(archivo_texto.read())

#Ahora al termiar de leer el texto le indicamos dónde queremos que se coloque el puntero
archivo_texto.seek(11)
print(archivo_texto.read()) #leera apartir de la posicion 11 (ía para morir....)

#Ahora lo queremos poner en medio del texto
archivo_texto.seek(len(archivo_texto.read())/2)
print(archivo_texto.read())

#Ahora colocamos el puntero al final de la primera linea
archivo_texto.seek(len(archivo_texto.readline()))
print(archivo_texto.read())