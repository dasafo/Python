from tkinter import *
from tkinter import filedialog



root=Tk()

def abreFichero():

	fichero=filedialog.askopenfilename(title="Abrir", initialdir="/home/david/", filetypes=(("Ficheros texto", "*.txt")
		, ("Ficheros PDF", "*.pdf"), ("Todos los ficheros", "*.*")))

	print(fichero) #nos dibuja la ruta en este caso

Button (root, text="Abrir fichero", command=abreFichero).pack()

root.mainloop()