from tkinter import *

raiz=Tk()

miFrame=Frame(raiz, width=500, height=600)
miFrame.pack()

#declaramos esta variable para el boton 'enviar'(ver final del código)
minombre=StringVar()


#Con grid() contruimos una tabla y situamos el Entry y el Label
cuadroNombre=Entry(miFrame, textvariable=minombre)
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="center")

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=1, column=1, padx=10, pady=10)
cuadroPass.config(show="*")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)
cuadroNombre.config(fg="green", justify="center")

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3, column=1, padx=10, pady=10)

textoComentario=Text(miFrame, width=18, height=5)
textoComentario.grid(row=4, column=1, padx=10, pady=10)
#Añadimos una scrollbar a la derecha del cuadro de texto y en el eje y
scrollVertical=Scrollbar(miFrame, command=textoComentario.yview)
#Lo posicionamos y con sticky le damos formato para que ocupe toda la altura del cuadro de texto
scrollVertical.grid(row=4, column=2, sticky="nsew")
#Ahora ponemos lo siguiente para que la barra se quede a la altura de donde estamos
textoComentario.config(yscrollcommand=scrollVertical.set)


#Con sticky alineamos el texto de las Label según (n,s,e,w,ne,se,sw,nw)
#Con pady y padx definimos la distancia entre los contendedores para que quede más limpio
nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

PassLabel=Label(miFrame, text="Password:")
PassLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

apellidoLabel=Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Dirección:")
direccionLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

comentariosLabel=Label(miFrame, text="Comentarios:")
comentariosLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)


#Añadimos ahora un botón, le decimos que al pulsar enviar, ponga David en nombre
def codigoBoton():
	minombre.set("David")

botonEnvio=Button(raiz, text="Enviar", command=codigoBoton)
botonEnvio.pack()

raiz.mainloop()