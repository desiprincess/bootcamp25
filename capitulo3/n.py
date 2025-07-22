import sys
def i(l): #nombre de la "fórmula"
    t = list(l)
    izq, drc = 0, len(t)-1
    while izq < drc: 
        t[izq], t[drc] = t[drc], t[izq] #me ahorro definir más de una variable
        izq += 1
        drc -=1 #para que vaya cambiando la posición
    return "".join(t)
salida = []
while True: 
    try: 
        l = input()
    
    except EOFError:
        break

    if len(l) % 2 == 0: #si el resto al dividirlo entre 2 es 0...
        res = i(l)
    else:
        res = l 
    salida.append(res)
sys.stdout.write("\n".join(salida)) #\n > salto de línea

