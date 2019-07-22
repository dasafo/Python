from io import open

archivo_texto=open("archivo.txt", "r+") # r+ es de lectura y escritura

#print(archivo_texto.readlines())

#Añadimos una linea en medio del documento

lista_texto=archivo_texto.readlines()

lista_texto[1]=" Esta línea ha sido incluida desde el exterior\n"

archivo_texto.seek(0)

archivo_texto.writelines(lista_texto)

archivo_texto.close()