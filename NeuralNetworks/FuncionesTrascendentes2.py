#Funcion exponencial f(x)=a^2
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.e**x
    #return 2**x

res = 1000

x=np.linspace(-1.0, 1.0, num=res)

y=f(x)

fig, ax=plt.subplots()

ax.plot(x, y)
ax.grid()
ax.axhline(y=0, color='r')
ax.axvline(x=0, color='r')

plt.show()