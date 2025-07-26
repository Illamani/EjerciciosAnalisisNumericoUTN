import RegresionLineal as RL
import numpy as np
import matplotlib.pyplot as plt

xIniciales = [0, 2, 4, 6, 9, 11, 12, 15, 17, 19]
yIniciales = [5, 6, 7, 6, 9, 8, 7, 10, 12, 12]

print(RL.constanteA1(xIniciales, yIniciales))
print(RL.constanteA0(xIniciales, yIniciales))

t_continuo = np.linspace(-3, 25, 100)
plt.scatter(xIniciales, yIniciales, color='black', label='Datos observados')
plt.plot(t_continuo, RL.regresionLineal(xIniciales, yIniciales, t_continuo), 'b-', label='Regresion Lineal')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()