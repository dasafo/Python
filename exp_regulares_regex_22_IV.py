import re

lista_nombres=['Carlos25',
                'Alina8',
                'Paula54',
                'Rosa22',
                'Sandra32',
                'Pedro24',
                'Paula24']

for elemento in lista_nombres:
    
    if re.findall('[o-t]',elemento): # nos muestra los nombres que contienen desde la o hasta la t

        print(elemento)

    if re.findall('^[O-T]',elemento): # nos muestra los nombres que empiezan desde la o hasta la t

        print(elemento)

    if re.findall('Paula[^0-25]',elemento): # nos muestra los nombres que empiezan por Paula y van a partir del 25 (^ 0-25 es negacion)

        print(elemento)