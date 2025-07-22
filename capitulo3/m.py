import sys

read = iter(sys.stdin.read().split())
p = int(next(read))
v = int(next(read))
suma = 0

for i in range(p): 
    for j in range(v):
        ventana1 = next(read)
        ventana2 = next(read)
        if  ventana1 =="#" or ventana2 == "#":
            suma += 1

sys.stdout.write(str(suma))

