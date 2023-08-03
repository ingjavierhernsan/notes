#Funciones potencia
#f(x)=x^a, aER
#Ejemplo: f(x)=x^2

import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**2

res = 100

x = np.linspace(-10, 10.0, num=res)

y = f(x)

fig, ax = plt.subplots()

ax.plot(x, y)
ax.grid()
ax.axhline(y=0, color='r')
ax.axvline(x=0, color='r')

plt.show()