import re

listaNombres=['Paco Ramirez',
                'Jorge Pla',
                'Marta Suarez',
                'Eva Fernandez',
                'Marta Mur',
                'Belén Pla']

for elemento in listaNombres:

    if re.findall('^Marta',elemento): #^ pilla los que comiencen por MArta

        print(elemento)


    if re.findall('Pla$',elemento): # $ pilla los que terminen por Pla

        print(elemento)
