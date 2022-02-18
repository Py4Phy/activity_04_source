# Solution for Problem 3

import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-6, 6, 601)
Y = np.sinc(X)

plt.plot(X, Y)
plt.xlabel("x")
plt.ylabel("y = sinc(x)")
plt.savefig("sinc.png")    # write plot to file
