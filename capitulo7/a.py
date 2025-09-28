n = int(input())

pila = []

for i in range(n): 
    linea = input()
    if linea.startswith("Depositan"): 
        titulo = linea[10:] #Esto hace que se guarde la linea pero obviando las primeras 10 letras en las que se encontraría la palabra "Depositan"
        pila.append(titulo) 
    elif linea.startswith("Retiran"): 
        if pila: #Verifica que la pila no está vacía.
            pila.pop() #para sacar el útlimo elemento que ha sido metido a la pila. 

if pila: 
    for libro in reversed(pila): #Para darle la vuelta a la pila y en vez de imprimir el último elemento qeu se ha metido, imprimir el primero.
        print(libro)
else: 
    print("No quedan libros")
