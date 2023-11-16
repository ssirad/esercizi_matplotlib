from math import *
import matplotlib.pyplot as plt
import random

#inizio
n=-1
while n<=0: #forzo il ciclo
    n=int(input("Quanti lanci vuoi fare? "))
dado1=[]
dado2=[]
somma=[]

#simulo i lanci di due dadi
for i in range (0,n):
    dado1.append(random.randint(1,6))

for i in range (0,n):
    dado2.append(random.randint(1,6))

#ora sommo i valori dei due lanci e li metto nella lista "somma"
for i in range (0,n):
    somma.append(dado1[i]+dado2[i])
   
#creo la lista delle frequenze di ogni somma
frequenze=[]
k=2
while k<13:
    cont=0
    for elemento in somma:
        if elemento==k:
            cont=cont+1
    frequenze.append(cont)
    k=k+1
   
#creo la lista delle frequenze relative
frequenzerelative=[]
for elemento in frequenze:
    frequenzerelative.append(elemento/n)

#creo i grafici  barre
xA=list()
for i in range(2,13):
    xA.append(i)
plt.figure(1)
plt.bar(xA, frequenze, width=0.4, color="cyan", label="dist.frequenze assolute" )
plt.legend()
plt.show()

#stampa le frequenze e le frequenze relative di ogni numero
for i in  range (0,11):
    print("valore",xA[i],"frequenza", frequenze[i], "frequenza relativa",frequenzerelative[i])
#fine
