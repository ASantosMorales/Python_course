import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 4*np.pi, 0.01)
y = np.sin(x)

plt.plot(x, y)
plt.show()