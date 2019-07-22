from tkinter import *
from tkinter import messagebox
import sqlite3


#-------------funciones--------------

def conexionBBDD():

	miConexion=sqlite3.connect("pracitca guiada/Usuarios")

	miCursor=miConexion.cursor()

	try:

		miCursor.execute('''
			CREATE TABLE DATOS_USUARIOS (
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			NOMBRE_USUARIO VARCHAR(50),
			PASSWORD VARCHAR(50),
			APELLIDO VARCHAR(10),
			DIRECCION VARCHAR(50),
			COMENTARIOS VARCHAR(100))
			''')

		messagebox.showinfo("BBDD", "BBDD creada con éxito")
	
	except:

		messagebox.showwarning("¡¡Atención!!", "La BBDD ya existe")


def salirAplicacion():

	valor=messagebox.askquestion("Salir", "¿Desea salir de la aplicación")

	if valor=="yes":
		root.destroy()

def limpiarCampos():

	miNombre.set("")
	miID.set("")
	miApellido.set("")
	miDireccion.set("")
	miPass.set("")
	textoComentario.delete(1.0, END) #Debe borrar desde el primer carácter (1.0) hasta el final (END)

def crear():

	miConexion=sqlite3.connect("pracitca guiada/Usuarios")

	miCursor=miConexion.cursor()

	datos=miNombre.get(),miPass.get(),miApellido.get(),miDireccion.get(),textoComentario.get("1.0", END)
	"""
	miCursor.execute("INSERT INTO DATOS_USUARIOS VALUES(NULL, '" + miNombre.get() +
		"','" + miPass.get() +
		"','" + miApellido.get() +
		"','" + miDireccion.get() +
		"','" + textoComentario.get("1.0", END) + "')")
	"""

	miCursor.execute("INSERT INTO DATOS_USUARIOS VALUES(NULL,?,?,?,?,?)",(datos)) #Null para que el ID sea autonumérico
	
	miConexion.commit()

	messagebox.showinfo("BBDD", "Registro insertado con éxito")


def leer():

	miConexion=sqlite3.connect("pracitca guiada/Usuarios")

	miCursor=miConexion.cursor()

	miCursor.execute("SELECT * FROM DATOS_USUARIOS WHERE ID=" + miID.get())

	elUsuario=miCursor.fetchall() #Para que nos lo devuelva en un array

	for usuario in elUsuario:

		miID.set(usuario[0])
		miNombre.set(usuario[1])
		miPass.set(usuario[2])
		miApellido.set(usuario[3])
		miDireccion.set(usuario[4])
		textoComentario.insert(1.0, usuario[5])

	miConexion.commit()

def actualizar():

	miConexion=sqlite3.connect("pracitca guiada/Usuarios")

	miCursor=miConexion.cursor()
	datos=miNombre.get(),miPass.get(),miApellido.get(),miDireccion.get(),textoComentario.get("1.0", END)
	
	"""
	miCursor.execute("UPDATE DATOS_USUARIOS SET NOMBRE_USUARIO='" + miNombre.get() + 
		"', PASSWORD='" + miPass.get() + 
		"', APELLIDO='" + miApellido.get() +
		"', DIRECCION='" + miDireccion.get() +
		"', COMENTARIOS='" + textoComentario.get("1.0", END) +
		"' WHERE ID=" + miID.get())
	"""

	miCursor.execute("UPDATE DATOS_USUARIOS SET NOMBRE_USUARIO=?,PASSWORD=?, APELLIDO=?, DIRECCION=?, COMENTARIOS=? " +
		"WHERE ID=" + miID.get(),(datos))


	miConexion.commit()

	messagebox.showinfo("BBDD", "Registro actualizado con éxito")


def eliminar():

	miConexion=sqlite3.connect("pracitca guiada/Usuarios")

	miCursor=miConexion.cursor()

	miCursor.execute("DELETE FROM DATOS_USUARIOS WHERE ID=" + miID.get())

	miConexion.commit()

	messagebox.showinfo("BBDD", "Registro borrado con éxito")

#---------------------------------------------------------------


root=Tk()


#-------Menu superior de menus desplegables---------

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexionBBDD)
bbddMenu.add_command(label="Salir", command=salirAplicacion)

borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar cambios", command=limpiarCampos)

crudMenu=Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear", command=crear)
crudMenu.add_command(label="Leer", command=leer)
crudMenu.add_command(label="Actualizar", command=actualizar)
crudMenu.add_command(label="Borrar", command=eliminar)

ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...")


barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

#---------------Comienzo de campos--------------

miFrame=Frame(root)
miFrame.pack()

miID=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miPass=StringVar()
miDireccion=StringVar()

cuadroID=Entry(miFrame, textvariable=miID)
cuadroID.grid(row=0, column=1, padx=10, pady=10)

cuadroNombre=Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="right")

cuadroPass=Entry(miFrame, textvariable=miPass)
cuadroPass.grid(row=2, column=1, padx=10, pady=10)
cuadroPass.config(show="#")

cuadroApellido=Entry(miFrame, textvariable=miApellido)
cuadroApellido.grid(row=3, column=1, padx=10, pady=10)

cuadroDireccion=Entry(miFrame, textvariable=miDireccion)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)

textoComentario=Text(miFrame, width=16, height=5)
textoComentario.grid(row=5, column=1, padx=10, pady=10)
scrollVert=Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")

textoComentario.config(yscrollcommand=scrollVert.set)


#-------Etiquetas.--------

idLabel=Label(miFrame, text="Id:")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

passLabel=Label(miFrame, text="Password:")
passLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

ApellidoLabel=Label(miFrame, text="Apellido:")
ApellidoLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Dirección:")
direccionLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

comentariosLabel=Label(miFrame, text="Comentarios:")
comentariosLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

#-------Aqui va el frame inferior con los botones----------

miFrame2=Frame(root)
miFrame2.pack()

botonCrear=Button(miFrame2, text="Create", command=crear)
botonCrear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

botonLeer=Button(miFrame2, text="Read", command=leer)
botonLeer.grid(row=1, column=1, sticky="e", padx=10, pady=10)

botonActualizar=Button(miFrame2, text="Update", command=actualizar)
botonActualizar.grid(row=1, column=2, sticky="e", padx=10, pady=10)

botonBorrar=Button(miFrame2, text="Delete", command=eliminar)
botonBorrar.grid(row=1, column=3, sticky="e", padx=10, pady=10)

#--------------------------------------------------------------------

root.mainloop()