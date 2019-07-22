import math

def raizcuadrada(listaNumeros):

    '''
    La función devuelve una lista con la 
    raíz cuadrada de los elementos numéricod pasadaos
    por parámetros en otr lista

    >>> lista=[]
    >>> for i in [4,9,16]:
    ...     lista.append(i)
    >>> raizcuadrada(lista)
    [2.0, 3.0, 4.0]

    '''

    return[math.sqrt(n) for n in listaNumeros]

#print(raizcuadrada([9,16,25,36]))

#importamos doctest para realizar una prueba dentro de los comentarios (>>>). 
import doctest
doctest.testmod()