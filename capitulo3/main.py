linea = 0

while True: 
    try:
        m = input()

        if linea % 2 == 0: 
            print(m[::-1])
        else:   
            print(m)
        linea += 1

    except EOFError:
        break



