#pilas y diccionarios. 
import sys

read = iter(sys.stdin.read().split())
n = int(next(read))

stack = [] #pila
opposite = {'F': 'B', 'B': 'F', 'L': 'R', 'R': 'L'}

for i in range(n):
    ins = next(read)
    if stack: #si hay algo en la pila, reviso el anterior y compruebo si es el opuesto. 
        ult = stack.pop()
        if ult == opposite[ins]: 
            continue #para que no haga nada.
        else: 
            stack.append(ult) #vuelvo a meter en la pila
            stack.append(ins) #meto nuevo.
    else: 
        stack.append(ins)
print(*stack)



