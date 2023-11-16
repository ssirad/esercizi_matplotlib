'''Scrivere un programma che rappresenti graficamente le seguenti funzioni:
1) y= 4sin(x)
2) y = |4 sin(x)|
3) y = 4sin(2x)

Seguire le istruzioni date
- Per la variabile indipendente creare una lista denominata x ottenuta campionando l’intervallo [0,2π]
in 100 punti equispaziati.
- Creare la lista contenente i valori di y utilizzando 3 differenti liste denominate Y1, Y2 e Y3 e utilizzando
un ciclo for
Output grafici:
Sono richiesti 3 tipi di grafici
Grafico 1: in un unico diagramma cartesiano rappresentare le 3 funzioni con queste caratteristiche
1) linea continua rossa
2) punti blu
3) linea tratteggiata gialla
Mettere la legenda, il titolo “ grafici sinusoidali”.

Grafico 2: solo il grafico della funzione 1 in rosso con linea tratteggiata e punti, titolo “legge oraria di un moto
armonico”

Grafico 3: tre grafici distinti in un’unica figura, con subplot'''

import matplotlib.pyplot as plt
import numpy as np
from random import randint

''' minimale, senza definire la funzione
all'esterno e senza passaggi di parametri, sfruttando
la funzione np.abs(y) che fa il valore assoluto di tutti
gli elementi dell'array delle ordinate '''

x = np.linspace(0, 2 * np.pi, 100) #calcola e crea una lista con campionati dell'intevallo [0.2 * π]

#scrive i tre valori di y [1) y= 4sin(x), 2) y = |4 sin(x)|, 3) y = 4sin(2x)]
y1 = 4 * np.sin(x)
y2 = np.abs(4 * np.sin(x))
y3 = 4 * np.sin(2 * x)

plt.figure(figsize=(8, 6))
plt.plot(x, y1, 'r-', label='y = 4sin(x)')
plt.plot(x, y2, 'bo', label='y = |4sin(x)|')
plt.plot(x, y3, 'y--', label='y = 4sin(2x)')
plt.legend()
plt.title('Grafici sinusoidali')
plt.xlabel('x')
plt.ylabel('y')

# Grafico 2
plt.figure()
plt.plot(x, y1, 'r--o')
plt.title('Legge oraria di un moto armonico')
plt.xlabel('x')
plt.ylabel('y')

# Grafico 3 (con i sottografici interni)
plt.figure(figsize=(12, 4))

# Sottografico 1
plt.subplot(131)
plt.plot(x, y1, 'r-')
plt.title('y = 4sin(x)')

# Sottografico 2
plt.subplot(132)
plt.plot(x, y2, 'bo')
plt.title('y = |4sin(x)|')

# Sottografico 3
plt.subplot(133)
plt.plot(x, y3, 'y--')
plt.title('y = 4sin(2x)')
plt.show()
