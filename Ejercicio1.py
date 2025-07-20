import numpy as np
import matplotlib.pyplot as plt
import os

def myFunction(x):
        return -0.5*x**2 + 2.5*x + 4.5  # Example: a quadratic function

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

metodosCerrados(5, 10, 200)
t_continuo = np.linspace(2.5, 12.5, 1000)
plt.scatter(xrArray, yrArray, color='black', label='Datos observados')
plt.plot(t_continuo, myFunction(t_continuo), 'b-', label='Sinusoide ajustada')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()


#x_values = np.linspace(-5, 5, 100) # 100 points between -5 and 5

#y_values = myFunction(x_values)

#plt.plot(x_values, y_values)
#plt.xlabel("x")
#plt.ylabel("f(x)")
#plt.title("Graph of f(x) = x^2 + 2x - 1")
#plt.show()