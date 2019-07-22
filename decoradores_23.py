def funcion_decoradora(funcion_parametro):

    def funcion_interior(*args, **kwargs): #con *args le estamos dciciendo que puede recibir un numero indeterminado de parámetros

        #Acciones adicionales que decoran/agregan

        print("Vamos a realizar un cálculo: ")

        funcion_parametro(*args, **kwargs)

        #Acciones adicionales que decoran/agregan

        print("Hemos terminado el cálculo")

    return funcion_interior


@funcion_decoradora #con @ le decimos que decore suma(justo debajo)
def suma(num1, num2, num3):

    print(num1+num2+num3)

@funcion_decoradora
def resta(num1,num2):

    print(num1-num2)
    
@funcion_decoradora
def potencia(base, exponente):

    print(pow(base,exponente))

suma(7,5,8)
resta(10,2)
potencia(base=5,exponente=3)