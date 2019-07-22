from distutils.core import setup
import py2exe
setup(

		name="paquetecalculos",
		version="1.0",
		description="Paquete de redondeo y potencia",
		author="David",
		author_email="balbla@bla.com",
		url="www.flipados.com",
		packages=["calculos", "calculos.redondeo_potencia"]


	)