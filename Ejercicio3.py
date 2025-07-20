import numpy as np
import matplotlib.pyplot as plt
import os

def myFunction(x):
        return 0.7*x**5 -8*x**4 + 44*x**3 - 90*x**2 + 82*x - 25 

def metodosCerrados(xl: int, xu: int, repeticiones: int):
	x = 0
	global xrArray, yrArray
	os.system('cls')
	print("--------------------------------------------------------------------------------------------------")
	while x < repeticiones:
		funcionXl = myFunction(xl)
		functionXu = myFunction(xu)
		#xr = (xl + xu) / 2 #Metodo de biseccion
		xr = xu - ((functionXu)*(xl-xu))/(funcionXl-functionXu) #Metodo de falsa posicion
		funcionXr = myFunction(xr)
		xrArray.insert(x, xr)
		yrArray.insert(x, funcionXr)
		x += 1
		print(str(x))
		print("	XL:    " + str(xl) + " / " + str(funcionXl))
		print("	XU:    " + str(xu) + " / " + str(functionXu))
		print("	XR:    " + str(xr) + " / " + str(funcionXr))
		print("	")
		if (funcionXr == 0):
			return xr
		if (funcionXr*funcionXl > 0):
			xl = xr
		else:
			xu = xr
	print("--------------------------------------------------------------------------------------------------")

xrArray = []
yrArray = []

metodosCerrados(0.5, 1, 5)
t_continuo = np.linspace(0.25, 1.25, 1000)
plt.scatter(xrArray, yrArray, color='black', label='Datos observados')
plt.plot(t_continuo, myFunction(t_continuo), 'b-', label='Sinusoide ajustada')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()
