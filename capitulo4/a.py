import sys

vocales = "aeiou"

def solve():
    palabras = input()
    nletras = len(palabras.replace(" ", "")) #.replace para que no cuente los espacios, sólo las letras(en este caso no hay más caracteres, sino contaría también las comas, los puntos, etc.)
    nvocales = 0
    for i in palabras: 
        if i in vocales: #si cada elemento que se encuentra en la variable "palabras" es alguno que se encuentra dentro de "vocales"
            nvocales += 1
    return nvocales, nletras

salida = []
n = int(input())
for j in range(n):
    v, l = solve() #separa el return en dos elementos
    salida.append(f"{v} {l}")
sys.stdout.write("\n".join(salida))

