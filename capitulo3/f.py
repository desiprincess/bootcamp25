import sys

read = iter(sys.stdin.read().split())
t = int(next(read))


for i in range(t):
    
    m = int(next(read))
    p = int(next(read))
    n = int(next(read))
    suma = 0

    for j in range(n): 
        suma += int(next(read))
    if n > m: 
        print("No cabemos")
    elif suma > m*p:
        print("Nos quedamos atrapados")

    else: 
        print("Todo bien")


    
