'''
Ripasso Python:
- stringhe
- liste
- tuple
- insiemi
- dizionari

ripasso liste:
- ordinate
- mutabili
- indicizzare
'''
import matplotlib.pyplot as plt
from math import *
x = []
for i in range(0, 201):
    x.append((pi/100)*i)

F1 = []
for i in range(0, 201):
    F1.append(x[i])
F2 = []
for i in range(0, 201):
    F2.append(pow(x[i], 2))
F3 = []
for i in range(0, 201):
    F3.append(sin(x[i]))

plt.plot(x, F1, label='funzione F1 ')
plt.plot(x, F2, label='funzione F2 ')
plt.plot(x, F3, label='funzione F3 ')
plt.xlabel('ascissa')
plt.ylabel('ordinata')
plt.title('Primo Grafico')
plt.legend()
plt.show()
