import sys

read = iter(sys.stdin.read().split())
n = int(next(read))
m = int(next(read))

sandias = []

maxim = -1
for i in range(n):
    s = 0
    fila = []
    for j in range(m):
        c = int(next(read))
        fila.append(c)
        s += c
    maxim = max(maxim,s)
    sandias.append(fila)

for i in range(m):
    s = 0
    for j in range(n):
        s += sandias[j][i]
    maxim = max(maxim,s)
print(maxim)

