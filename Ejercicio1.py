import numpy as np
import matplotlib.pyplot as plt
import os

def myFunction(x):
        return -0.5*x**2 + 2.5*x + 4.5  # Example: a quadratic function

def metodosCerrados(xl: int, xu: int, repeticiones: int, xrArray, yrArray):
	x = 0
	xr = 0
	os.system('cls')
	print("--------------------------------------------------------------------------------------------------")
	while x < repeticiones:
		funcionXl = myFunction(xl)
		functionXu = myFunction(xu)
		xrViejo = xr

		#xr = (xl + xu) / 2 #Metodo de biseccion
		xr = xu - ((functionXu)*(xl-xu))/(funcionXl-functionXu) #Metodo de falsa posicion
		
		funcionXr = myFunction(xr)
		xrArray.insert(x, xr)
		yrArray.insert(x, funcionXr)
		if(x != 0):
			errorRelativo = ((xr - xrViejo)/xr)  * 100
			print("Error relativo porcental: " + str(errorRelativo) + " %")
		x += 1
		print(str(x))
		print("	XL:    " + str(xl) + " / " + str(funcionXl))
		print("	XU:    " + str(xu) + " / " + str(functionXu))
		print("	XR:    " + str(xr) + " / " + str(funcionXr))
		print("	")
		if (funcionXr*funcionXl > 0):
			xl = xr
		else:
			xu = xr
	print("--------------------------------------------------------------------------------------------------")

xrArray = []
yrArray = []

metodosCerrados(5, 10, 3, xrArray, yrArray)
t_continuo = np.linspace(2.5, 12.5, 1000)
plt.scatter(xrArray, yrArray, color='black', label='Datos observados')
plt.plot(t_continuo, myFunction(t_continuo), 'b-', label='Sinusoide ajustada')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()