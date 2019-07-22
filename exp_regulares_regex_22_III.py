import re

lista_nombres=['http://google.es',
                'ftp://elpais.es',
                'http://google.com',
                'ftp://twitter.com',
                'http://españadesarrollo.es',
                'hombres',
                'mujeres',
                'mascotas',
                'niños',
                'niñas']

for elemento in lista_nombres:
    
    if re.findall('es$',elemento): # $ pilla los que comiencen por es

        print(elemento)

    if re.findall('^ftp',elemento): #^ pilla los que comiencen por ftp

        print(elemento)

    if re.findall('[ñ]',elemento): # para que busque las ñ

        print(elemento)

    if re.findall('niñ[oa]s',elemento): # para que con ese patron 

        print(elemento)