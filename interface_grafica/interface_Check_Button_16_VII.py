from tkinter import *

root=Tk()

root.title("Ejemplo")

playa=IntVar()
montagna=IntVar()
rural=IntVar()

def opcionesViaje():

	opcionEscogida=""

	if(playa.get()==1):
		opcionEscogida+=" playa"

	if(montagna.get()==1):
		opcionEscogida+=" montaña"

	if(rural.get()==1):
		opcionEscogida+=" rural"

	textoFinal.config(text=opcionEscogida)


foto=PhotoImage(file="interface_grafica/avion.png")
Label(root, image=foto).pack()

frame=Frame(root)
frame.pack()

Label(frame, text="Elige destinos", width=50).pack()
#Con onvalue(offvlue) le decimos que el valor almacenado en playa, cuando se seleccione(se quite), valga 1(0)
Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack() 
Checkbutton(frame, text="Montaña", variable=montagna, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Rural",  variable=rural, onvalue=1, offvalue=0, command=opcionesViaje).pack()

textoFinal=Label(frame)
textoFinal.pack()

root.mainloop()