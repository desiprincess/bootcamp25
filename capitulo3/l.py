import sys

read = iter(sys.stdin.read().split())
t = int(next(read))

for i in range(t):
    n = int(next(read))
    c = int(next(read))
    b = [int(next(read)) for j in range(n)] #lo convierte en una lista
    if c in b: 
        print("YES")
    else:
        print("NO")


