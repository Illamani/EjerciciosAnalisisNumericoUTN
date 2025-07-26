#Este ejercicio es usar logica y definicion
#Primero se saca el valor de y en la fila 4, que es y = 1/2*8+5/2 => 6.5 y se completa la siguiente columna xi*yi => 52
#Ahora falta toda la primera columna, teniendo y = 6 entonces 
#La sumatoria de x sobre N + la sumatoria de Y sobre N me da 115 / 7
#(xi + 57) / 7 + 5.92857 = 115/7 => xi1 = (115/7 -5.92857)*7 - 57
#xi = 16.5

import RegresionLineal as RL
import numpy as np
import matplotlib.pyplot as plt

xIniciales = [9, 12, 9, 8, 10, 11, 7]
yIniciales = [6, 10, 5, 6.5, 7, 8, 9]

print(RL.constanteA1(xIniciales, yIniciales))
print(RL.constanteA0(xIniciales, yIniciales))

t_continuo = np.linspace(0, 20, 100)
plt.scatter(xIniciales, yIniciales, color='black', label='Datos observados')
plt.plot(t_continuo, RL.regresionLineal(xIniciales, yIniciales, t_continuo), 'b-', label='Regresion Lineal')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()