#numero di teste nel lancio di 3 monete
import matplotlib.pyplot as plt
from random import randint

n = int(input('quanti lanci si vuole fare? \n'))
while n < 0:
	n = int(input('quanti lanci si vuole fare? \n'))

moneta1 = []
moneta2 = []
moneta3 = []
pari1 = 0
pari2 = 0
pari3 = 0
dispari1 = 0
dispari2 = 0
dispari3 = 0

for i in range(n):
	moneta1.append(randint(0,1))
	if moneta1[i] == 0:
		pari1 += 1
	elif moneta1[i] == 1:
		dispari1 += 1
	moneta2.append(randint(0,1))
	if moneta2[i] == 0:
		pari2 += 1
	else:
		dispari2 += 1
	
	moneta3.append(randint(0,1))
	if moneta3[i] == 0:
		pari3 += 1
	else:
		dispari3 += 1

plt.figure('numero di teste nel lancio di 3 monete')
plt.bar(1,pari1, color = 'crimson')
plt.bar(2,dispari1, color = 'gainsboro')
plt.bar(3,pari2, color = 'crimson')
plt.bar(4,dispari2, color = 'gainsboro')
plt.bar(5,pari3, color = 'crimson')
plt.bar(6,dispari3, color = 'gainsboro')
plt.title('numero di teste nel lancio di 3 monete')
plt.ylabel('numero di lanci')
plt.show()
