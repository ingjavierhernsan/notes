#Funcion logaritmo logb(x)=n <=> x=b^n
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.log2(x)

res = 1000

x=np.linspace(0.01, 256.0, num=res)

y=f(x)

fig, ax=plt.subplots()

ax.plot(x, y)
ax.grid()
ax.axhline(y=0, color='r')
ax.axvline(x=0, color='r')

plt.show()