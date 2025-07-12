wth = input()
gr = int(input())

pasean = []
if gr>=20 and wth=="Soleado": 
    pasean.append("Adrian")
if gr>15 or wth=="Soleado": 
    pasean.append("Barbara")
if wth in ("Soleado", "Nublado"): 
    pasean.append("Carmen")
if wth != "Tormenta": 
    pasean.append("Dario")

print("Vienen a pasear:"," ".join(pasean))

