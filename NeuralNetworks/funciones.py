#Pagina para las formulas WolframAlpha

import numpy as np
import matplotlib.pyplot as plt

def sigmoid(a):
    return 1/(1+np.exp(-a))

def step(x):
 return np.piecewise(x, [x<0.0, x>0.0], [0, 1])

def relu(a):
   return [np.piecewise(i, [i<0.0, i>=0.0], [0, i]) for i in a]

def tanh(a):
   return (np.exp(a) - np.exp(-a)) / (np.exp(a) + np.exp(-a))

def softmax(v):
   v_exp = np.exp(v)
   v_exp_sum = np.sum(v_exp)
   return [a/v_exp_sum for a in v_exp]

x = np.linspace(10, -10, 100)

plt.plot(x, sigmoid(x), color='red')
plt.plot(x, step(x), color='yellow')
plt.plot(x, relu(x), color='blue')
plt.plot(x, tanh(x), color='green')
plt.plot(x, softmax(x), color='pink')

plt.grid()
plt.show()