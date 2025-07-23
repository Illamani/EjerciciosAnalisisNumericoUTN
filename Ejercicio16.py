import numpy as np
import matplotlib.pyplot as plt

# Definir la función de la serie de Fourier con N términos
def fourier_sawtooth(t, N_terms=100):
    """
    Aproximación de la onda diente de sierra usando N términos de la serie de Fourier.
    
    Parámetros:
        t (array): Array de tiempos donde evaluar la función.
        N_terms (int): Número de términos de la serie (por defecto 100).
        
    Retorna:
        Array con la aproximación de la onda diente de sierra.
    """
    approximation = np.zeros_like(t)
    for n in range(1, N_terms + 1):
        coefficient = 2 * (-1)**(n + 1) / (np.pi * n)
        approximation += coefficient * np.sin(2 * np.pi * n * t)
    return approximation

# Crear un array de tiempos desde -1.5 hasta 1.5 para visualizar periodicidad
t = np.linspace(-1.5, 1.5, 5000)

# Calcular la aproximación con 100 términos
f_approx = fourier_sawtooth(t, N_terms=100)

# Graficar
plt.figure(figsize=(10, 5))
plt.plot(t, f_approx, label=f"Aproximación con 100 términos", color="blue", linewidth=1.5)
plt.title("Aproximación de la Onda Diente de Sierra con Serie de Fourier (100 términos)")
plt.xlabel("Tiempo $t$")
plt.ylabel("Amplitud $f(t)$")
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend()
plt.show()