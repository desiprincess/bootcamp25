import sys 

read = iter(sys.stdin.read().split())
n = int(next(read))

calidad = set() #una colección desordenada de elementos, los sets no se pueden sort(), por lo que lo convierto luego en una lista.
cafe = {} #crear diccionario
for i in range(n): 
    q = int(next(read))
    e = next(read)
    calidad.add(q)
    #lista = [java]
    if q in cafe:  #cafe[q] = [e]
                    #lista
        cafe[q].append(e) #Mete todas las e en una lista que tengan el mismo key.
    else: 
        cafe[q] = [e] 

calidad = list(calidad) #convierto el set en una lista
calidad.sort()

for key in calidad: 
    values = cafe.get(key) #Es una lista que contiene todas las "e" dentro de cada número(key).
    if len(values) > 1: 
        values.sort()
    for j in values:
        print(key, j)
