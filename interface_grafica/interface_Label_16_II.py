from tkinter import *

root=Tk()

miFrame=Frame(root, width=500, height=400)

miFrame.pack()

miImagen=PhotoImage(file="interface_grafica/atom.gif")

Label(miFrame, image=miImagen).place(x=100, y=200) #hubicamos la imagen dentro de la ventana

#Para poner texto en vez de imagen
#Label(miFrame, text="Hola pringados", fg="red", font=("Comic Sans Ms", 22)).place(x=100, y=200) #hubicamos el texto dentro de la ventana

root.mainloop()