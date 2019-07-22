class Areas:


    def areaCuadrado(lado):

        """
        Calcula el área de un cuadrado
        """

        return "El área del cuadrado es: " + str(lado*lado)

    def areaTriangulo(base,altura):

        """
        Calcula el área de un triangulo metiendo la base y la altura
        """

        return "El área del triángulo es: " + str((base*altura)/2)


#Para que nos imprima la documentacion(comentarios) asociada a esa funcion
#print(areaCuadrado.__doc__)

#Otra forma de que nos saque la documentacion
help(Areas.areaTriangulo)


