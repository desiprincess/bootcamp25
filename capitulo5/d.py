import sys 

read = iter(sys.stdin.read().split())
n = int(next(read))

problemas = set()
compe = {}
for i in range(n): 
    s = int(next(read))
    p = int(next(read))
    problemas.add(s) #.add para añadirlo al set. Es como el append en el caso de un lista.
    if s in compe: 
        compe[s].append(p)
    else: 
        compe[s] = [p]

problemas = list(problemas) #lo convierto en una lista porque el set no puede ser ordenado.
problemas.sort(reverse = True) #Para que ordene de forma descendiente en vez de ascendiente

for key in problemas:
    value = compe.get(key) 
    if len(value) > 1: 
        value.sort()
    for i in value:
        print(key, i)

