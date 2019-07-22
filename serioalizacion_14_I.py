import pickle

lista_nombres=["Pedro", "Ana", "Maria", "Isabel"]

fichero_binario=open("lista_nombres", "wb") #escritura binaria 'wb'

#volcamos el contenido
pickle.dump(lista_nombres, fichero_binario)

fichero_binario.close()

#Si queremos podemos borrar el archivo binario para gastar menos memoria
del (fichero_binario)