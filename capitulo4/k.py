import sys 

read = iter(sys.stdin.read().split())
n = int(next(read))
m = int(next(read))

tablero = [next(read) for _ in range(n)]

tablero2 = [[""for _ in range(m)] for _ in range(n)]

dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]

for i in range(n):  
    for j in range(m): 
        if tablero[i][j] == "*": 
            tablero2[i][j] = "F" #== es para comprobar.
        else: 
            minas = 0
            for k in range(8): 
                pi, pj = i + dy[k], j + dx[k]
                if 0 <= pi < n and 0 <= pj < m: 
                    if tablero[pi][pj] == "*": 
                        minas += 1
            if minas > 0: 
                tablero2[i][j] = str(minas)
            else: 
                tablero2[i][j] = " "

for filas in tablero2:
    print("".join(filas))
