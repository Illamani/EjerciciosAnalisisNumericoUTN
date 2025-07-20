import numpy as np
import matplotlib.pyplot as plt
import os

def myFunction(x):
        return -0.5*x**2 + 2.5*x + 4.5  # Example: a quadratic function

def biseccion(xl: int, xu: int, repeticiones: int):
	x = 0
	os.system('cls')
	print("--------------------------------------------------------------------------------------------------")
	while x < repeticiones:
		xr = (xl + xu) / 2
		funcionXr = myFunction(xr)
		funcionXl = myFunction(xl)
		functionXu = myFunction(xu)
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

biseccion(5, 10, 5)

#x_values = np.linspace(-5, 5, 100) # 100 points between -5 and 5

#y_values = myFunction(x_values)

#plt.plot(x_values, y_values)
#plt.xlabel("x")
#plt.ylabel("f(x)")
#plt.title("Graph of f(x) = x^2 + 2x - 1")
#plt.show()