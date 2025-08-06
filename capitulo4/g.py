import sys    

read = iter(sys.stdin.read().split())
n = int(next(read))

tablero = []
for i in range(n):
    for j in range(8):
        tablero.append(next(read))

#si sumo las posiciones, es decir i+j, me doy cuenta de que esa suma siempre va a posicionar a las "w" es un nºpar y a la "b" en un inpar.

tablero2 = []
for i in range(8):
    linea = []
    for j in range(8):
        if (i+j) % 2 == 0 and tablero[i][j] != "W":
            linea.append("X")
        elif (i+j) % 2 == 1 and tablero[i][j] != "B": 
            linea.append("X")
        else: 
            linea.append(tablero[i][j])
    tablero2.append("".join(linea))
print("\n".join(tablero2))
            
#LINEAS PARES 
#w = pares
#b = impares

#LINEAS IMPARES 
#w = impares
#b = pares
