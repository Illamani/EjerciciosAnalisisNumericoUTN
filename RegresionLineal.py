def sumatoriaProductoCartesiano(xList: list, yList: list):
	sumatoria = 0
	for x in  range(len(xList)):
		sumatoria += xList[x] * yList[x]
		x =+ 1 
	return sumatoria * len(xList)

def sumatoriaX(xList : list):
	sumatoria = 0
	for x in xList:
		sumatoria += x
	return sumatoria

def sumatoriaY(yList: list):
	sumatoria = 0
	for y in yList:
		sumatoria += y
	return sumatoria

def sumatoriaXCuadrada(xList: list):
	sumatoria = 0
	for x in xList:
		sumatoria += x**2
	return sumatoria * len(xList)

def constanteA1(xList: list, yList: list):
	return (sumatoriaProductoCartesiano(xList, yList) - sumatoriaX(xList) * sumatoriaY(yList)) / (sumatoriaXCuadrada(xList) - sumatoriaX(xList)**2)

def constanteA0(xList: list, yList: list):
	return sumatoriaY(yList)/len(xList) - constanteA1(xList, yList)*sumatoriaX(xList)/len(xList)

def regresionLineal(xList: list, yList: list, x):
	return constanteA0(xList, yList) + constanteA1(xList, yList) * x

