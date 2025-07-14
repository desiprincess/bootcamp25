import sys

read = iter(sys.stdin.read().split())
n = int(next(read))
numeros = [int(next(read)) for i in range(n)]
mn = min(numeros)
my = max(numeros)
print(mn, my)
