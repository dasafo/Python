from tkinter import *

#Creamos la raiz
raiz=Tk()
raiz.title("Ventana de pruebas")

#Podemos fijar el tamaño de la ventana e impedr redimensionar
#raiz.resizable(0,1) #Widht=False(0), Hight=True(1)

#Ponemos icono en la ventana
#raiz.wm_iconbitmap("@atom.xbm")

#Dimensiones d ela ventana de la raiz
#raiz.geometry("650x350")

#Color del fondo de la raiz
raiz.config(bg="blue")

#Ahora ponemos un tipo de borde con un grosor determinado
raiz.config(bd=15)
raiz.config(relief="sunken")
#Le decimos que al poner el cursor encima del frame, este cambie
raiz.config(cursor="circle")



#Creamos un Frame y lo metemos dentro de la raiz con pack(Frame<Raiz)
miFrame=Frame()

miFrame.pack(side="left", anchor="n") #Con 'side' anclamos el frame a la izquierda, y con anchor anclamos al norte 'n'

#miFrame.pack(fill="x", expand="True") #Es como el de arriba pero con fill fijamos a lo largo de todo eje de x (con expand) el frame entero

miFrame.config(width="650", height="350")
miFrame.config(bg="red")

#Ahora ponemos un tipo de borde con un grosor determinado
miFrame.config(bd=35)
miFrame.config(relief="groove")
#Le decimos que al poner el cursor encima del frame, este cambie
miFrame.config(cursor="hand2")


#mainloop() genera una especie de bucle infinito para mantener la ventana abierta. Debe ir siempre al final.
raiz.mainloop()