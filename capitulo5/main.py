import sys

def bubbleSort(a):
    n = len(a)
    for i in range(n): 
        cambio = False
        for j in range(0, n-i-1): #en este range porque los últimos i elementos ya están colocados.
            if a[j] > a[j+1]: 
                a[j], a[j+1] = a[j+1], a[j] #Los intercambia para ordenarlos.
                cambio = True
        if cambio == False: #Cuando ya está todo ordenado
                break

def insertionSort(a):
    for i in range(1, len(a)): 
        key = a[i]
        j = i-1

        while j >= 0 and key<a[j]:
            a[j+1] = a[j]
            j -= 1 
        a[j+1] = key

def selectionSort(a):
    n = len(a)
    for i in range(n-1): 

        min = i 

        for j in range(i+1, n):
            if a[j] < a[min]: 
                min = j 
        a[i], a[min] = a[min], a[i]

def mergeSort(a): 



read = iter(sys.stdin.read().split())
n = int(next(read))

a = [int(next(read)) for i in range(n)]
bubbleSort(a)
#insertionSort(a) 
#selectionSort(a)
print(*a)

