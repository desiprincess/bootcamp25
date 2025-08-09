import sys

read = iter(sys.stdin.read().split())
n = int(next(read))

a = [int(next(read)) for i in range(n)] 
# a = [10,7,1,22,20]
a.sort() #para ordenar la lista de menor a mayor. A partir de aquí, a ya está ordenada.
# a = [1,7,10,20,22]

restas = []
for i in range(n-1): 
    res = a[i+1]-a[i]
    restas.append(res)
print(min(restas))
