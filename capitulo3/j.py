import sys 

read = iter(sys.stdin.read().split())
suma = 0
salida = []

while True: 
    try: 
        n = int(next(read))
    except StopIteration: 
        break
    suma += n
    salida.append(str(suma))
sys.stdout.write(" ".join(salida))



    
