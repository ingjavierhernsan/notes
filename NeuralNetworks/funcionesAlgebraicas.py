#Funcion lineal
#f(x)=mx+b

import matplotlib.pyplot as plt
import numpy as np

def f(m, x, b):
    return m*x+b

res = 100
m = -2
b = 5

x = np.linspace(-10, 10.0, num=res)

y = f(m, x, b)

fig, ax = plt.subplots()

ax.plot(x, y)
ax.grid()
ax.axhline(y=0, color='r')
ax.axvline(x=0, color='r')

plt.show()