import sys 

def solve():
    m = int(next(read))
    n = int(next(read))
    e = float(next(read))

    matriz = []
    for i in range(m): 
        filas = []
        for j in range(n):
            a = float(next(read))
            if a <= e:
                a = "0.000000"
            else: 
                a = f"{a:.6f}"
            filas.append(a)
        matriz.append(" ".join(filas))
    print("\n".join(matriz)) #le digo como quiero que es´ten separados las listas dentro de la matriz del output.

read = iter(sys.stdin.read().split())
t = int(next(read))

for _ in range(t): 
    solve()
