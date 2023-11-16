import matplotlib.pyplot as plt
from math import *

def det(r, s, t, w):
    d = r*w - s*t
    return d


def cramer(a1, b1, c1, a2, b2, c2):
    d = det(a1, b1, a2, b2)
    if d == 0:
        print('sistema indeterminato o impossibile')
    else:
        dx = det(c1, b1, c2, b2)
        dy = det(a1, c1, a2, c2)
        x = dx/d
        y = dy/d
        return x, y


def v1(t):
    vasca1 = 10+15*t
    return vasca1


def v2(t):
    vasca2 = 200-25*t
    return vasca2


x1 = list()
for i in range(0, 13):
    x1.append(i)

x2 = list()
for i in range(12, 21):
    x2.append(i)

vasca1_1 = list()
for i in range(0, 13):
    vasca1_1.append(v1(x1[i]))

vasca1_2 = list()
for i in range(12, 21):
    vasca1_2.append(190)

x3 = list()
for i in range(0, 9):
    x3.append(i)

x4 = list()
for i in range(8, 21):
    x4.append(i)

vasca2_1 = list()
for i in range(0, 9):
    vasca2_1.append(v2(x3[i]))

vasca2_2 = list()
for i in range(8, 21):
    vasca2_2.append(0)


# trovo il punto di intersezione con il metodo di Cramer
xp, yp = cramer(15, -1, -10, 25, 1, 200)


# GRAFICI

plt.plot(x1, vasca1_1, label='vasca 1', color='red')
plt.plot(x2, vasca1_2, color='red')
plt.xlabel('x, tempo in minuti')
plt.ylabel('y, volume in litri')
plt.grid()
plt.plot(x3, vasca2_1, label='vasca 2', color='blue')
plt.plot(x4, vasca2_2, color='blue')
# evidenziare il punto di intersezione delle due rette
plt.plot(xp, yp, color='green', marker='o')
plt.xlabel("punto di intersezione: ")
plt.legend()
plt.show()
