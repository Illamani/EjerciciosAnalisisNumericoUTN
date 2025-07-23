import numpy as np
import matplotlib.pyplot as plt
import os

def myFunction(x):
        return -2.75*x**3 + 18*x**2 - 21*x - 12   

def metodosCerrados(xl: int, xu: int, repeticiones: int):
	x = 0
	xr = 0
	global xrArray, yrArray
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

metodosCerrados(-1, -0.2, 5)
t_continuo = np.linspace(-.5, -0.2, 1000)
plt.scatter(xrArray, yrArray, color='black', label='Datos observados')
plt.plot(t_continuo, myFunction(t_continuo), 'b-', label='Sinusoide ajustada')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()
