import RegresionLineal as RL
import numpy as np
import matplotlib.pyplot as plt

xIniciales = [6, 7, 11, 15, 17, 21, 23, 29, 29, 37, 39]
yIniciales = [29, 21, 29, 14, 21, 15, 7, 7, 13, 0, 3]

print(RL.constanteA1(xIniciales, yIniciales))
print(RL.constanteA0(xIniciales, yIniciales))

t_continuo = np.linspace(-3, 45, 100)
plt.scatter(xIniciales, yIniciales, color='black', label='Datos observados')
plt.plot(t_continuo, RL.regresionLineal(xIniciales, yIniciales, t_continuo), 'b-', label='Regresion Lineal')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()