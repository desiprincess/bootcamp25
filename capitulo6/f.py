import sys
from collections import deque 

def BFS(sr, sc): 
    q = deque([(sr, sc, 1)]) #Hace que la cola sea una lista de tuplas, es decir, (e, e, e), (e, e, e)...
        #deque = double-ended queue.
                #Indica donde empieza la cola. 
                        #1 para contar la primera casilla.
    visitado[sr][sc] = True #marco el punto de partida como ya visitado.

    dirs = ((0, -1), (-1, 0), (0, 1), (1, 0)) #Direcciones a las que podemos movernos. 

    while q: 
        r, c, dist = q.popleft()    
        #fila, columna y distancia (casillas recorridas) actual.
        if r == tr and c == tc: #Si ya estamos donde queremos llegar
            return dist 
        
        for row, col in dirs: #cada elemento en una lista de pares.
            nrow, ncol = r + row, c + col #Para que revise las casillas alrededor. 

            if not (0 <= nrow < h and 0 <= ncol < w): 
                continue #límites para cuando esté en los laterales. 

            if visitado[nrow][ncol]: 
                continue

            celda = laberinto[nrow][ncol]
            if celda == "#":
                continue

            visitado[nrow][ncol] = True #marcamos como ya visitado.
            q.append((nrow, ncol, dist+1)) #(()) para que lo entienda como un solo elemento

    return -1
        
read = iter(sys.stdin.read().split())
w = int(next(read))
h = int(next(read))

laberinto = []
for _ in range(h): 
    laberinto.append(list(next(read)))

sr = sc = tr = tc = -1

for i in range(h): 
    for j in range(w): 
        if laberinto[i][j] == "E": 
            sr, sc = i, j    #Ubica la entrada y la salida.
        elif laberinto[i][j] == "S": 
            tr, tc, = i, j

visitado = [[False] * w for _ in range(h)] #Una matriz donde todoslos elementos son False. 
print(BFS(sr, sc))
