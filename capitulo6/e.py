import sys

def dfs(r, c):  #row, column
    if r == tr and c == tc: 
        return 0    #si ya nos encontramos en el objetivo no han habido saltos.
    
    visitado[r][c] = 1   #marcar la celda en la que nos encontramos como ya visitada.

    for row, col in dirs: 
        nrow, ncol = r + row, c + col    #prueba cada vecino
         #n = next

        if not(0 <= nrow < n and 0 <= ncol < n): 
            continue  

        if visitado[nrow][ncol]: 
            continue 
        
        celda = lago[nrow][ncol]
        if celda == '.': 
            continue

        res = dfs(nrow, ncol)
        if res != -1: #por aquí sí hay camino 
            return res + 1 #suma saltos

    return -1 #no hay camino 

read = iter(sys.stdin.read().split())
n = int(next(read))

lago = []
for _ in range(n): 
    lago.append(list(next(read)))

#sr = start row     sc = start column     tr = target row     tc = target column
sr = sc = tr = tc = -1 #de esta forma todas las variables tienen el mismo valor.

for i in range(n): 
    for j in range(n): 
        if lago[i][j] == 'R': 
            sr, sc = i, j   #Ubico donde empieza y donde acaba.
        elif lago[i][j] == 'C': 
            tr, tc = i, j 

visitado = [bytearray(n) for _ in range(n)]  #una lista de caracteres inicializados a 0 en cada fila [0, 0, 0...,0]

#Direcciones por la que permite moverse (izq, arriba, der, abajo)
dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))

visitado[sr][sc] = 1 #marcar que la R está visitada para no tener que volver a ella.

print(dfs(sr, sc))
