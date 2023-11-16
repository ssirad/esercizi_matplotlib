import matplotlib.pylab as plt
from math import *
import numpy as np

def es_1():
    def f(t):
        f = 10 * exp(-t) * sin(4 * t)
        return f
    
    x = []
    for i in range(0, 100):
        x.append(pi / 100 * i)
    
    y = []
    for i in range(0, 100):
        y.append(10 * exp(-x[i]) * sin(4 * x[i]))
    
    plt.subplot(2, 1, 1)
    plt.plot(x, y, 'ko-')
    plt.title("Un esposenziale somrzato")
    plt.subplot(2, 1, 2)
    plt.plot(x, np.abs(y), 'ko-')
    plt.title("Valore assoluto di un esponeniale smorzato")
    plt.show()
es_1()

def es_2():
    plt.figure(1)
    nomi = ['A1', 'A2', 'A3']
    datiA = [4, 5, 6]
    plt.bar(nomi, datiA, align='center', width=0.35, color='cyan')
    
    plt.figure(1)
    
    xA = [1, 2, 3]
    xB = [1.4, 2.4, 3.4]
    datiB = [8, 6, 7]
    plt.bar(xA, datiA, align='center', width=0.35, color='cyan')
    plt.bar(xB, datiB, align='center', width=0.35, color='cyan')
    plt.legend()
    plt.xticks(xA)
    
    plt.show()

es_2()
