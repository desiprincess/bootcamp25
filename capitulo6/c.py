def numeroTriangular(x):
    if x == 1: 
        return 1
    else: 
        return numeroTriangular(x-1) + x 


x = int(input())
print(numeroTriangular(x))

