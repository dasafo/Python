# -*- coding: utf-8 -*-


from setuptools import setup

setup(
    name="paquetecalculos",
    version="1.0",
    description="Paquete de redondeo y pontencia",
    author="David",
    author_email="d.salasforns@gmail.com",
    url="",
    packages=["calculos", "calculos.redondeo_potencia"],
    scripts=[]

)

'''
Este archivo se usa para poder utilizar paquetes desde cualquier directorio del PC sin tener que especificar su directorio. 

Para ejecutarlo Abrir Terminal en la carpeta donde esté setup.py---> escribir 'python setup.py sdist' (con sdist paquete distribuible) que crea las carpetas 'dist' y 'paquetescalculos.egg-info'.

En dist tenemos el paquete comprimido que podemos exportar donde queramos(llamado paquetecalculos-1.0tar.gz)

Para instalarlo ponemos en terminal 'pip3 install paquetecalculos-1.0.tar.gz'
'''
