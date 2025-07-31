import sys 

def solve(texto):
    res = "*" #no es 0 porque no es un número sino un cáracter
    for i in range(len(texto)):#"i" va a ser el nº de la posición
        if texto[i] == " ":
            res += "**"
        else:
            res += " " + texto[i] + " *"
    borde = bordes(len(res))
    return f"{borde}\n{res}\n{borde}"

def bordes(m): 
    res = ""
    for i in range(m):
        res += "*"
    return res 
    
n = int(input())
salida = []

for i in range(n): 
    texto = input()
    salida.append(solve(texto))
print("\n".join(salida))
