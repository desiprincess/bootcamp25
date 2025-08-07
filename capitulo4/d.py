import sys

read = iter(sys.stdin.read().split())
n = int(next(read))
m = int(next(read))

mesa = []
for _ in range(n):
    mesa.append(next(read))

filas = [False] * n
col = [False] * m

for i in range(n):
    for j in range(m):
        if mesa[i][j] == "#": #la j posición dentro la i posición
            filas[i] = True
            col[j] = True

salida = []
for i in range(n): 
    ans = []
    for j in range(m): 
        if filas[i] or col[j]: #AND Y OR SOLO ACEPTAN VALORES BOOLEANOS (VERDADERO O FALSO)
            ans.append("#")
        else: 
            ans.append(".")
    salida.append("".join(ans))

print("\n".join(salida))
