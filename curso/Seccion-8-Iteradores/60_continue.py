#cancelamos la ejecucion de todo el ciclo y emesamos desde arriba

print("antes")
i = 1
while i < 10:
    i += 1
    if(i == 5):
        continue
    elif(i == 8):
        break
    print(i)
else:
    print("El break corta el else del while tambien")

print("despues")