import sys

def binarySearch(l, c, izq, der):
    if izq > der:
        return "NO" #Caso base para que la recursión termine.
    m = (izq+der) // 2 #va a la posición del medio
    if l[m] == c: 
        return "YES"
    elif l[m] > c: 
        return binarySearch(l, c, izq, m-1) #recursivo = llamo a la misma función varias veces. Aquí declaro los nuevos límites.
    else:
        return binarySearch(l, c, m+1, der) #+-1 porque esos números ya han sido descartados antes y no hace falta volverlos a revisar.

read = iter(sys.stdin.read().split())
n = int(next(read))
l = [int(next(read)) for i in range(n)]
l.sort() #ordenar la lista
q = int(next(read))

for i in range(q): 
    c = int(next(read))
    print(binarySearch(l, c, 0, len(l)-1))
