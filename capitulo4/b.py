import sys 

salida = []
read = iter(sys.stdin.read().split())
n = int(next(read))

h1 = [int(next(read)) for i in range(n)]
#lo convierte en listas
h2 = [int(next(read)) for j in range(n)]

for k in range(n):
    res = h1[k] + h2[k]
    salida.append(res)

print(*salida) #"*salida, sep=" "" entre las comillas puedo poner el separador que quiera, pero por defecto es un espacio asi que en este caso no hace falta ponerlo.

