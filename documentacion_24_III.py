def compruebaEmail(mailUsuario):

    '''
    esta función compruebaEmail comprueba un mail en busca de la @
    Si tiene una @ es correcto, si tiene más de una incorrecto, si la @
    está al final es incorrecto

    >>> compruebaEmail('david@temas.es')
    True

    >>> compruebaEmail('david@temas.es@')
    False

    >>> compruebaEmail('davidtemas.es')
    False

    >>> compruebaEmail('david@@temas.es')
    False

    '''

    arroba=mailUsuario.count('@')

    if(arroba!=1 or mailUsuario.rfind('@')==(len(mailUsuario)-1) or mailUsuario.find('@')==0):
        return False
    else:
        return True


#importamos doctest para realizar una prueba dentro de los comentarios (>>>). 
import doctest
doctest.testmod()