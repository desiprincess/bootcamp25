import sys

read = iter(sys.stdin.read().split())
n = int(next(read))
m = int(next(read))

lienzo = []
for i in range(n):
    lienzo.append(next(read))

for i in range(n-1): 
    for j in range(m-1):  #porque sino se pasa del rango (out of bounds)
        if lienzo[i][j] == lienzo[i][j+1] == lienzo[i+1][j] == lienzo[i+1][j+1]: 
            print("NO ORIGINAL")
                exit()  #si ya se cumple se deja de ejecutar el programa entero.
                    print("ORIGINAL") #está colocado aquí porque es cuando ya ha terminado de leer TODO, no solo una sola linea.

