def cuentaAtras(n):
    print(n)
    if n <= 1:  #Caso base para que pare la recursión.
        exit()
    elif n > 1: 
        cuentaAtras(n-1) #recursion

n = int(input())
cuentaAtras(n)



