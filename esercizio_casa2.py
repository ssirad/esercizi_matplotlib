import random

n -= 1
while n = 0:
    n = int(input("Quanti lanci vuoi fare? "))
tuttiilanci = []

for k in range(0, n):
    lancio = []

    for i in range(0, 3):
        var = random.randint(0, 1)
        if var == 1:
            lancio.append("T")
        else:
            lancio.append("C")
    tuttiilanci.append(lancio)

ncroce = []
for elementi in tuttiilanci:
    cont = 0
    for i in range(0,3):
        if elemento[i] == "T":
            cont += 1
    ncroce.append(cont)

frequenze = []
k = 0
while k < 4:
    contat = 0
    for elemento in ncroce:
        if elemento == k:
            contat += 1
    frequenze.append(contat)
    k += 1

frequenzerelative = []
for elemento in frequenze:
    frequenzerelative.append(elemento/n)

xA = list()
for i in range(0, 4):
    xA.append(i)
plt.figure(1)
plt.bar(xA, frequenze, width=0.4, color= "cryan", label= "dist.f.lanci")
plt.legend()
plt.show()
plt.figure(2)
plt.bar(xA, frequenzerelative, width=0.4, color="green", label="dist.f.rel")
plt.legend()
plt.show()

for i in range(0, 4):
    print("vaore", aX[i], "freq= ", frequenze[i], "frel= ", frequenzerelative[i])
