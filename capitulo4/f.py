import sys

read = iter(sys.stdin.read().split())
l = int(next(read))

tostada1 = []
for i in range(l): 
    tostada1.append(next(read))

#next(read) #como no lo uso como tal no me hace falta ponerle nombre
tostada2 = []
for j in range(l):
    tostada2.append(next(read))

mermelada = 0
for i in range(l):
    for j in range(l): 
        if tostada1[i][j] == "#": 
            mermelada += 1 
if mermelada == 0: #está alineado con las líneas.
    print("NO LLEVABA MERMELADA")

elif tostada1 == tostada2: 
    print("HA HABIDO SUERTE")
else: 
    print("TRAGEDIA")
