import RegresionLineal as RL
import numpy as np
import matplotlib.pyplot as plt

xIniciales = [1, 2, 3, 4, 5, 6, 7, 8, 9]
yIniciales = [1, 1.5, 2, 3, 4, 5, 8, 10, 13]

print(RL.constanteA1(xIniciales, yIniciales))
print(RL.constanteA0(xIniciales, yIniciales))

t_continuo = np.linspace(0, 11, 100)
plt.scatter(xIniciales, yIniciales, color='black', label='Datos observados')
plt.plot(t_continuo, RL.regresionLineal(xIniciales, yIniciales, t_continuo), 'b-', label='Regresion Lineal')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()