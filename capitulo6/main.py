import sys

def row(fila, j, minimo):
    if j == len(fila): 
        return minimo

    if fila[j] < fila[minimo]: 
        minimo = j #voy actualizando el minimo numero de la fila
    return row(fila, j+1, minimo)

def col(matriz, i, j, min_row):
    if i == len(matriz):
        return True 
    if matriz[i][j] > min_row: #si algun numero de la columna es mayor al que hemos declarado coo el minimo deja de cumplir lo que pide el problema.
        return False
    return col(matriz, i+1, j, min_row)

def saddle(matriz, i): #la funcion que me va a devolver las coordenadas.
    if i == len(matriz): 
        return -1, -1       #caso base 
    j = row(matriz[i], 1, 0)
    min_row = matriz[i][j] #asumimos que el min row va a er el max col. 
    if col(matriz, 0, j, min_row): 
        return i, j #para que me devuelva unicamente las coordenadas.
    return saddle(matriz, i+1) #i+1 para que vaya leyendo todas las filas.

def solve(): 
    n = int(next(read)); m = int(next(read))
    matriz = []
    for j in range(n):
        linea = []
        for k in range(m): 
            linea.append(int(next(read)))
        matriz.append(linea)               #matriz construida. 
    return saddle(matriz, 0)

read = iter(sys.stdin.read().split())
t = int(next(read))

salida = []
for i in range(t): 
    x, y = solve()
    salida.append(f"{x} {y}")
print("\n".join(salida))

            
