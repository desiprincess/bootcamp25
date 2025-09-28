#queue; First in, first out
from collections import deque

n = int(input())

#cola = [deque(), deque(), deque()] 

cola = []
for i in range(3): 
    p = input().split()
    d = deque(p)
    cola.append(d)
    #para meter cada linea en su cola correspondiente.

while True: 
    try: 
        linea = input()
    except EOFError:
        break 
    if not linea: #si es una línea vacía para de ejecutarse el programa.
        break 
    
    partes = linea.split() #para separar los comandos por partes.
    cmd = partes[0] #como poner que la frase startswith...

    if cmd == "MOVER": 
        origen = int(partes[1])
        destino = int(partes[2])
        if cola[origen]: 

            m = cola[origen].popleft()
            cola[destino].append(m)

    if cmd == "AGREGAR": 
        l = partes[1] #aquí no hay un origen como tal
        destino = int(partes[2])
        cola[destino].append(l)

    if cmd == "ATENDER":
        at = int(partes[1])
        if cola[at]: 
            cola[at].popleft()

for c in cola: #porque hay tres colas.
    if c: #mirando si hay algo dentro de las colas o no.
        print(*c)
    else: 
        print("NO HAY NADIE") 
