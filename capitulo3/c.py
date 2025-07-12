import sys

pi = float(3.141592)
read = iter(sys.stdin.read().split())
n = int(next(read))
salida = []


for i in range(n): 
    f = int(next(read))
    x = float(next(read))

    if f == 1: 
        ans = x**2*pi 
    elif f == 2: 
        ans = x*x
    
    elif f == 3: 
        y = float(next(read))
        ans = x * y
    else: 
        y = float(next(read))
        ans = (x * y)/2
    salida.append(f"{ans:.5f}")
sys.stdout.write("\n".join(salida))
