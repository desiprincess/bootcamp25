import sys
from collections import deque 

def BFS(sr,sc):
    q = deque([(sr, sc, 0)])
    visitado[sr][sc] = True 

    dirs = ((0, 1), (-1, 0), (1, 0), (0, -1))

    while q: 
        r, c, saltos = q.popleft()
        if r == tr and c == tc:
            return saltos 

        for row, col in dirs: 
            nrow, ncol = r + row, c + col
            
            if not (0 <= nrow < n and 0 <= ncol < n): 
                continue 
            
            if visitado[nrow][ncol]: 
                continue

            celda = lago[nrow][ncol] 
            if celda == ".": 
                continue 

            visitado[nrow][ncol] = True 
            q.append((nrow, ncol, saltos+1))

    return -1

read = iter(sys.stdin.read().split())
n = int(next(read))

lago = []
for _ in range(n): 
    lago.append(list(next(read)))

sr = sc = tr = tc = -1 

for i in range(n):
    for j in range(n): 
        if lago[i][j] == "R": 
            sr, sc = i, j
        if lago[i][j] == "C":
            tr, tc = i, j

visitado = [[False] * n for _ in range(n)]
print(BFS(sr, sc))

