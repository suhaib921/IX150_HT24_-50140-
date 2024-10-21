import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Givna data (RSA bitstorlekar och tider)
bitstorlekar = np.array([100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200])
tider = np.array([1.7754, 1.2068, 2.2104, 0.3446, 23.1459, 23.6331, 26.9525, 118.2895, 111.3844, 846.8159, 1027.0917])

# Definiera en exponentiell funktion för anpassning: y(x) = e^(a*x) + b
def exp_func(x, a, b):
    return np.exp(a * x) + b

# Utför kurvanpassning
popt, pcov = curve_fit(exp_func, bitstorlekar, tider)

# Generera punkter för en kontinuerlig exponentiell kurva (från 100 till 4096 bitar)
x_fit = np.linspace(100, 4096, 1000) 
y_fit = exp_func(x_fit, *popt)

# Förutsäg tider för större nyckelstorlekar (1024, 2048, 4096 bitar)
stora_nyckelstorlekar = np.array([1024, 2048, 4096])
förutsagda_tider = exp_func(stora_nyckelstorlekar, *popt)

# Plotta de ursprungliga data med en logaritmisk y-axel
plt.scatter(bitstorlekar, tider, color='blue', label="Ursprungliga Data")
plt.plot(x_fit, y_fit, color='red', label="Anpassad Exponentiell Kurva")  

# Använd en logaritmisk skala för y-axeln för att matcha det logaritmiska diagrammet
plt.yscale('log')

# Plotta förutsägelser för större nyckelstorlekar
plt.scatter(stora_nyckelstorlekar, förutsagda_tider, color='green', label="Förutsagt för Större Nycklar")

plt.xlabel('RSA Nyckelstorlek (bitar)')
plt.ylabel('Tid (sekunder)')
plt.title('Tid vs RSA Nyckelstorlek med Exponentiell Anpassning (Log-y)')
plt.legend()
plt.show()
print(f"Förutsagda tider för 1024-bitars, 2048-bitars och 4096-bitars RSA-nycklar: {förutsagda_tider}")
