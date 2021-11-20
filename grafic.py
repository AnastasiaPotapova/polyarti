import numpy as np


def signal(msg):
    const = 10
    periods = []
    t = np.linspace(1, 100, 1000)
    x_volts = const * np.sin(t / (2 * np.pi))
    j = -1
    for i in range(1000):
        if i // 100 != j:
            j = i // 100
            periods.append([])
        try:
            x_volts[i] *= msg[j]
            periods[-1].append([msg[j], x_volts[i]])
        except Exception as e:
            x_volts[i] *= 1
            periods[-1].append([1, x_volts[i]])
    return [periods, x_volts]


def inter(msg):
    periods = signal(msg)[0]
    for i in range(len(periods) - 1):
        for j in range(20):
            try:
                periods[i][100 - j - 1][1] = periods[i][100 - j - 1][1] + periods[i + 1][j][1]
            except Exception:
                print(len(periods), i, len(periods[i]), 100 - j - 1, j)
                exit()
        for j in range(20):
            periods[i + 1][j][1] = periods[i][100 - j - 1][1] + periods[i + 1][j][1]
    return periods

