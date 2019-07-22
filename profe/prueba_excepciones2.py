def divide():

	try:

		op1=(float(input("Introduce el primer número: ")))

		op2=(float(input("Introduce el primer número: ")))

		print("La división es: " + str(op1/op2))

	except ValueError:

		print("El valor introducio es erróneo")

	except ZeroDivisionError:

		print("No se puede dividir por 0")

	finally:

		print("Cálculo finalizado")

divide()