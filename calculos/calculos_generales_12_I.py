#Creamos estos modulos dentro del paquete calculos_12 (que hemos indicado como paquete gracias al archivo __init__.py dentro de esa carpeta)

def sumar(op1,op2):
	print("El resultado de la suma es: ", op1+op2)

def restar(op1,op2):
	print("El resultado de la resta es: ", op1-op2)

def multiplicar(op1,op2):
	print("El resultado de la multiplicación es: ", op1*op2)

def dividir(dividendo, divisor):
	print("El resultado de la division es: ", dividendo/divisor)

def potencia(base,exponente):
	print("El resultado de la potencia es: ", base**exponente)

def redondear(numero):
	print("El resultado del redondeo es: ", round(numero))