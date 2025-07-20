import numpy as np
import matplotlib.pyplot as plt
import os

def myFunction(x):
        return -2.75*x**3 + 18*x**2 - 21*x - 12   

def biseccion(xl: int, xu: int, repeticiones: int):
	x = 0
	os.system('cls')
	print("--------------------------------------------------------------------------------------------------")
	while x < repeticiones:
		xr = (xl + xu) / 2
		funcionXr = myFunction(xr)
		funcionXl = myFunction(xl)
		functionXu = myFunction(xu)
		if(x > 0):
			errorPorcentual = abs(((xr - xrVieja) / xr ) * 100)
			print("Error Porcentual : " + str(errorPorcentual) + " %")
		xrVieja = xr
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



biseccion(0.5, 2, 10)