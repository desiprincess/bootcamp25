abc = input().split()
x = int(abc[0])&int(abc[1])
y = x|int(abc[2])
z = y ^ int(abc[1])
print(x, y, z)
