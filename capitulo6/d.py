def flechaUp(n): 
    linea = ['#'] * (n-1)
    linea.append('\n')
    linea = "".join(linea)
    if n == 1: 
        return ''
    else: 
        return flechaUp(n-1) + linea
    

def flechaDown(n):
    linea = ['#'] * n
    linea.append('\n')  # [e, e, e...,\n]
    linea = "".join(linea)
    if n == 1:
        return linea
    else: 
        return linea +flechaDown(n-1) 

x = int(input())
print(flechaUp(x)+flechaDown(x))

