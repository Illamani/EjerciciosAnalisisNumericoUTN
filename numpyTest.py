import numpy as np
import matplotlib.pyplot as plt

# Datos
meses = np.array([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5])
radiacion = np.array([122, 188, 245, 311, 351, 359, 308, 287, 260, 211, 159, 131])

# Ecuación ajustada
def R(t):
    return 244.75 - 108.87 * np.cos(np.pi * t / 6) - 42.63 * np.sin(np.pi * t / 6)

# Gráfica
t_continuo = np.linspace(0, 12, 1000)
plt.scatter(meses, radiacion, color='black', label='Datos observados')
plt.plot(t_continuo, R(t_continuo), 'b-', label='Sinusoide ajustada')
plt.scatter(7.5, R(7.5), color='red', label='Pronóstico agosto (7.5)')
plt.xlabel('Meses (centrados)')
plt.ylabel('Radiación solar (W/m²)')
plt.legend()
plt.grid()
plt.show()