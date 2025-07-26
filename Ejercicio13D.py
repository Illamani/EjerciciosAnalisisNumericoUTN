import RegresionLineal as RL
import numpy as np
import matplotlib.pyplot as plt

xIniciales = [2, 3, 5, 7, 8]
yIniciales = [14, 20, 32, 42, 44]

print(RL.constanteA1(xIniciales, yIniciales))
print(RL.constanteA0(xIniciales, yIniciales))

t_continuo = np.linspace(0, 10, 100)
plt.scatter(xIniciales, yIniciales, color='black', label='Datos observados')
plt.plot(t_continuo, RL.regresionLineal(xIniciales, yIniciales, t_continuo), 'b-', label='Regresion Lineal')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()