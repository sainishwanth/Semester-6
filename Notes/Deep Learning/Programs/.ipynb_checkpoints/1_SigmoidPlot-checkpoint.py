import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-10, 10, 1000)
y = 1 / (1 + np.exp(-x) )
plt.figure(figsize=(10, 5))
plt.plot(x, y)
plt.legend(['sigmoid function'])
plt.show()
