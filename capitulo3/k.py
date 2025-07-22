salida = []

while True: 
    try: 
        l = input()
        salida.append(l)
    except EOFError: 
        break

print(salida[-1])


