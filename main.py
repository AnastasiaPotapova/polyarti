#создает тренирующую и тестовую выборку
import random

f = open("train_msg.txt", 'w')
for i in range(100):
    n = random.randint(1, 10)
    dt = []
    for i in range(n):
        dt.append(random.randint(0, 1))
    f.write(''.join([str(x) for x in dt]) + '\n')
f.close()

f = open("test_msg.txt", 'w')
for i in range(100):
    n = random.randint(1, 10)
    dt = []
    for i in range(n):
        dt.append(random.randint(0, 1))
    f.write(''.join([str(x) for x in dt]) + '\n')
f.close()
