import numpy as np

#Funciones Matriciales

def sumatoriaCoseno(xList: list, vel: int):
	sum = 0
	for x in xList:
		sum += np.cos(vel * x)
	return sum

def sumatoriaCosenoCuadrado(xList: list, vel: int):
	sum = 0
	for x in xList:
		sum += (np.cos(vel * x))**2
	return sum

def sumatoriaSeno(xList: list, vel: int):
	sum = 0
	for x in xList:
		sum += np.sin(vel * x)
	return sum

def sumatoriaSenoCuadrado(xList: list, vel: int):
	sum = 0
	for x in xList:
		sum += (np.sin(vel * x))**2
	return sum

def SumatoriaSenoCoseno(xList: list, vel: int):
	sum = 0
	for x in xList:
		sum += np.sin(vel * x) * np.cos(vel * x)
	return sum

def sumatoriaY(yList: list):
	sum = 0
	for y in yList:
		sum += y
	return sum

def sumatoriaYSeno(xList: list, yList: list, vel: int):
	sum = 0
	y = 0
	for x in xList:
		sum += np.sin(vel * x) * yList[y] 
		x += 1
	return sum

def sumatoriaYCoseno(xList: list, yList: list, vel: int):
	sum = 0
	y = 0
	for x in xList:
		sum += np.cos(vel * x) * yList[y] 
		x += 1
	return sum

def velocidadAngular(T: int):
	return (2*np.pi)/T

#Funciones Determinantes

def determinantes(matriz):
	return round(np.linalg.det(matriz),10)

#valoresInicialesX = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#valoresInicialesY = [122, 188, 245, 311, 351, 359, 308, 287, 260, 211, 159, 131]


valoresInicialesX = [0, 2, 4, 5, 7, 8.5, 12, 15, 20, 22, 24]
valoresInicialesY = [7.3, 7, 7.1, 6.4, 7.4, 7.2, 8.9, 8.8, 8.9, 7.9, 7]


velocidad = velocidadAngular(24)
sumCos = sumatoriaCoseno(valoresInicialesX, velocidad)
sumCosCuadrado = sumatoriaCosenoCuadrado(valoresInicialesX, velocidad)
sumSen = sumatoriaSeno(valoresInicialesX, velocidad)
sumSenCuadrado = sumatoriaSenoCuadrado(valoresInicialesX, velocidad)
sumSenCos = SumatoriaSenoCoseno(valoresInicialesX, velocidad)
sumY = sumatoriaY(valoresInicialesY)
sumYCos = sumatoriaYCoseno(valoresInicialesX, valoresInicialesY, velocidad)
sumYSen = sumatoriaYSeno(valoresInicialesX, valoresInicialesY, velocidad)

matriz = [[len(valoresInicialesX), sumCos, sumSen], [sumCos, sumCosCuadrado, sumSenCos], [sumSen, sumSenCos, sumSenCuadrado], [sumY, sumYCos, sumYSen]]

determinanteBase = determinantes([matriz[0], matriz[1], matriz[2]])
determinanteX = determinantes([matriz[3], matriz[1], matriz[2]])
determinanteY = determinantes([matriz[0], matriz[3], matriz[2]])
determinanteZ = determinantes([matriz[0], matriz[1], matriz[3]])

print(determinanteX/determinanteBase)
print(determinanteY/determinanteBase)
print(determinanteZ/determinanteBase)