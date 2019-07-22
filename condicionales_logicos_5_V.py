print("Asignatura optativa Ano 2017")
print("Asignaturas: Informática gráfica - Software - Usabilidad y accesibilidad")
opcion=input("Escribe la asignatura escogida: ")

#Pasamos lo escrito a minusculas
asignatura=opcion.lower()

if asignatura in ("informática gráfica", "software", "usabilidad y accesibilidad"):
	
	print("Asignatura elegida: " + asignatura)

else:

	print("No existe la asignatura")		
