import sys

read = iter(sys.stdin.read().split())
salida = []
e_i = int(next(read))

while True:
    try:
        e_j = int(next(read))
    except StopIteration:
        break

    if e_j > e_i: 
        res = "S"
    elif e_j < e_i: 
        res = "B"
    else: 
        res = "I"
    e_i = e_j
    salida.append(res)

sys.stdout.write ("".join(salida))

