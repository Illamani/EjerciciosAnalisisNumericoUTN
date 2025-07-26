#Este ejercicio requiere una logica para la conversion de F(x) a G(x), siendo G(x) una reescritura de F(x) donde se iguala a cero0
#para luego reemplazar ese cero por una x de F(x)
#Algo que no se como hacerlo y no tengo tiempo para pensarlo, por eso uso directamente G(X)
#Algo similar pasa con como saber si es divergente o convergente esta funcion en un entorno, en teoria se puede hacer derivando y buscando
#Pero no se como hacerlo y no tengo tiempo de pensarlo
#f(x) = 2sin(x^2)-x
#g(x) = 2sin(x^2)

import numpy as np
import matplotlib.pyplot as plt
import os
import math

def functionGx(x):
    return 2*np.sin(math.sqrt(x))

def functionFx(x):
	return 2*np.sin(math.sqrt(x)) - x

def metodoPuntoFijo(xInicial: int, repeticiones: int):
	x = 0
	global xrArray, yrArray
	os.system('cls')
	print("--------------------------------------------------------------------------------------------------")
	while x < repeticiones:
		xInicialPlus = functionGx(xInicial)
		functionXInicialPlus = functionFx(xInicialPlus)
		functionXInicial = functionFx(xInicial)

		xrArray.insert(x, xInicialPlus)
		yrArray.insert(x, functionXInicialPlus)

		print(str(x))
		if(x != 0):
			errorRelativo = abs(((xInicialPlus - xInicial)/xInicialPlus))  * 100
			print("	Error relativo porcental: " + str(errorRelativo) + " %")

		print("	X(" + str(x) + "): " +str(xInicial) + " / " + str(functionXInicial))
		print("	X(" + str(x + 1) + "): " + str(xInicialPlus) + " / " + str(functionXInicialPlus))
		print("	")
		xInicial = xInicialPlus
		x += 1
	print("--------------------------------------------------------------------------------------------------")

xrArray = []
yrArray = []

metodoPuntoFijo(0.5 , 4)
t_continuo = [np.linspace(-0.5, 1.25, 1000)]
plt.scatter(xrArray, yrArray, color='black', label='Datos observados')
#plt.plot(t_continuo, functionFx(t_continuo), 'b-', label='Sinusoide ajustada')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()
