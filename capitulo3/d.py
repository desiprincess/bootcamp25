import sys 

read = iter(sys.stdin.read().split())
n = int(next(read))
p = int(next(read))
salida = []

for i in range(p):
    a = int(next(read))
    if a == n: 
        punt = "1p"
    elif abs(n-a) <= 5: 
        punt = "0.5p" 
    elif abs(n-a) <=10: 
        punt = "0.25p" 
    else: 
        punt = "0p" 

    salida.append(punt)
sys.stdout.write(" ".join(salida))


