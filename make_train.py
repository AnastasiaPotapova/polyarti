import numpy as np
from Noise import noise
from grafic import signal, inter

msgs = open("train_msg.txt", 'r')
inp = open("train_y.txt", 'w')
outp = open("train_x.txt", 'w')
for i in range(10000):
    msg = [1 if x == '1' else -1 for x in list(msgs.readline())]
    sig = inter(msg)
    for i in sig:
        a = []
        b = []
        for j in i:
            a.append(j[1])
            b.append(j[0])
        y_volts = noise(a)
        outp.write(' '.join([str(x) for x in y_volts]))
        outp.write('\n')
        inp.write('\n'.join([str(x) for x in b]))
        inp.write('\n')
msgs.close()
inp.close()
outp.close()
