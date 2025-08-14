def fibonacci(x):
    #1 1 2 3 5 8 13...
    #Caso base
    if 1 <= x <= 2: 
        return 1
    else: 
        return fibonacci(x-1) + fibonacci(x-2)
    

x = int(input())
print(fibonacci(x))

