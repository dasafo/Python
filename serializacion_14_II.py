import pickle

#Ahora rescatamos el archivo binario

fichero=open("lista_nombres", "rb") #leer información binaria 'rb'

lista=pickle.load(fichero)

print(lista)