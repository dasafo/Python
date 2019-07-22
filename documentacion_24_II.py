def areaTriangulo(base,altura):

    """
    Calcula el area de un triangulo. Ahora comprobamos con una prueba que funciona, si todo va correcto no aparecerá nada, sino saldrá un error.

    >>> areaTriangulo(3,6)
    'El área del triángulo es: 9.0'

    >>> areaTriangulo(4,5)
    'El área del triángulo es: 1.0'

    >>> areaTriangulo(9,3)
    'El área del triángulo es: 13.5'

    


    """

    return "El área del triángulo es: " + str((base*altura)/2)

#importamos doctest para realizar una prueba dentro de los comentarios (>>>). 
import doctest
doctest.testmod()