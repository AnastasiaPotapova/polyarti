import matplotlib.pyplot as plt
import numpy as np
from grafic import signal, inter
from gr_op import noise

msg = [-1, 1]
const = 10
X = np.linspace(1, 100, 100)
Y = signal(msg)[1]
plt.subplot(3, 1, 1)
plt.plot(X, Y[:100])
plt.show()

Y_ = list(Y[:20])
for i in range(10):
    for j in range(60):
        Y_.append(Y[i*100 + j + 20])
    for j in range(20):
        Y_.append(Y[i*100 + j] + Y[i*100 + j + 20])
X = np.linspace(1, 100, len(Y_))
plt.subplot(3, 1, 1)
plt.plot(X[:100], Y_[:100])
plt.show()

periods = inter(msg)
Y = []
for i in range(len(msg)):
    for j in range(len(periods[i][:-20])):
        Y.append(periods[i][j][1])
for j in range(len(periods[-1][-20:])):
    Y.append(periods[-1][j][1])
X = np.linspace(1, 100, len(Y))
plt.subplot(3, 1, 1)
plt.plot(X[:100], Y[:100])
plt.show()

Y = noise(Y)
plt.subplot(3, 1, 1)
plt.plot(X[:100], Y[:100])
plt.show()

