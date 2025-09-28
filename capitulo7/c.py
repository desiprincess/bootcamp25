import sys

read = iter(sys.stdin.read().split())
n = int(next(read))

freq = {} #diccionario
for i in range(n):
    id = int(next(read))
    if id in freq: 
        freq[x] += 1
    else: 
        freq[x] = 1
'''
Podría hacerse con una sola línea de la siguiente forma: 

freq[x] = freq.get(x, 0) + 1

Esta forma evita el uso de if/else cuando quiero leer una clave que a lo mejor no existe aún. (El 0 es el valor que se le proporciona por defecto a dicha clave.)
'''

for drink_id, count in freq.items(): #freq items te da los pares pero desordenados. 
    maxc = 0
    bestid = None 
    if count > maxc: 
        maxc = count
        bestid = drink_id
    if count == maxc: 
        if drink_id < bestid: #para que cumpla mi condición.
            bestid = drink_id
print(bestid)

        


