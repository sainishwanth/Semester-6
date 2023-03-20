import numpy as np
import matplotlib.pyplot as plt

def tanh(x):
    return 2 / (1+ np.exp(-2*x)) - 1

x = np.linspace(-10, 10, 100)
y = tanh(x)
plt.plot(x, y)
plt.title('Hyperbolic Tangent Function')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
