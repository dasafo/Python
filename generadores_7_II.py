def generaPares2(limite):

	num=1

	while num<limite:

		yield num*2

		num=num+1

devuelvePares=generaPares2(10)
#Para que nos devuelve el primer valor que tiene almacenado en su interior
print(next(devuelvePares))

print("Aquí pordía ir más código....")

print(next(devuelvePares))

print("Aquí pordía ir más código....")

print(next(devuelvePares))

