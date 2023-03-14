import numpy as np
import matplotlib.pyplot as plt

def relu(x):
    return np.maximum(0, x)

x = np.linspace(-10, 10, 100)
y = relu(x)
plt.plot(x, y)
plt.title('Rectified Linear Unit Function')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
