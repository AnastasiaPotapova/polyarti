import matplotlib.pyplot as plt
import numpy as np
from grafic import signal, inter
from Noise import noise

msg = [-1, 1, 1, -1, 1, 1, -1]
const = 10
X = np.linspace(1, 100, 1000)
Y = signal(msg)[1]
plt.subplot(3, 1, 1)
plt.plot(X, Y)
plt.show()

Y_ = list(Y[:20])
for i in range(10):
    for j in range(60):
        Y_.append(Y[i*100 + j + 20])
    for j in range(20):
        Y_.append(Y[i*100 + j] + Y[i*100 + j + 20])
print(len(Y_))
X = np.linspace(1, 100, len(Y_))
plt.subplot(3, 1, 1)
plt.plot(X, Y_)
plt.show()

Y = noise(Y_)
X = np.linspace(1, 100, len(Y))
plt.subplot(3, 1, 1)
plt.plot(X, Y)
plt.show()

