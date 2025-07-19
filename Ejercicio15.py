import numpy as np
import matplotlib.pyplot as plt
import math

meses = np.array([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5])
radiacion = np.array([122, 188, 245, 311, 351, 359, 308, 287, 260, 211, 159, 131])

def Ri(radMes:list):
	x = 0
	for rad in  radMes:
		x += rad
	return x/radMes.__len__()

def RCos(radMes:list, meses:list):
	x = 0.5
	value = 0
	for rad in radMes:
		value += rad*math.cos(x*math.pi/6)
		x += 1
	return value

def RSin(radMes: list, meses: list):
	x = 0.5
	value = 0
	for rad in radMes:
		value += rad*math.sin(x*math.pi/6)
		x += 1
	return value	

print(Ri(radiacion))
print(RCos(radiacion, meses))
print(RSin(radiacion, meses))