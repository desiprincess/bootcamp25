import  sys

read = iter(sys.stdin.read().split())
n = int(next(read))

a = [int(next(read)) for i in range(n)]
b = [int(next(read)) for j in range(n)]

for k in range(n):
    if k % 2 != 0: 
        a[k], b[k] = b[k], a[k] #asignación múltiple
       
print(*a)
print(*b)
