#Funcion polinomicas
#P(x)=anx^n + an-1x^n-1 + ... + a2x^2 + a1x+x a1
#Ejemplo: P(x)=2x^7 - x^4 + 3x^2 + 5

import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 2*x**8 - x**4 + 3*x**2 + 4

res = 100

x = np.linspace(-10, 10.0, num=res)

y = f(x)

fig, ax = plt.subplots()

ax.plot(x, y)
ax.grid()
ax.axhline(y=0, color='r')
ax.axvline(x=0, color='r')

plt.show()