from tkinter import *
from tkinter import messagebox #Importamos para hacer ventanas emergentes

root=Tk()

#Para la ventana emergente que saldrá al presionar Acerca de... y Licencia, realizamos esta fucnión
def infoAdicional():
	messagebox.showinfo("Procesador de David", "Procesador de textos 2018")

def avisoLicencia():
	messagebox.showwarning("Licenca", "Producto bajo licencia de David")

def salirAplicacion():
	#valor=messagebox.askquestion("Salir", "¿Deseas pirarte?")
	valor=messagebox.askokcancel("Salir", "¿Deseas pirarte?")

	#if valor=="yes":
	if valor==True:
		root.destroy()

def cerrarDocumento():
	valor=messagebox.askretrycancel("Reintentar", "No es posible cerrar el documento")
	
	if valor==False:
		root.destroy()


barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

archivoMenu=Menu(barraMenu, tearoff=0) #tearoff quitamos la linea separadora de arriba
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como...")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command=cerrarDocumento)
archivoMenu.add_command(label="Salir", command=salirAplicacion)


archivoEdicion=Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoHerramientas=Menu(barraMenu, tearoff=0)

archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Licencia", command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de...", command=infoAdicional)

#indicamos cómo se llaman cada desplegable
barraMenu.add_cascade(label="Menú", menu=archivoMenu)
barraMenu.add_cascade(label="Edición", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)


root.mainloop()