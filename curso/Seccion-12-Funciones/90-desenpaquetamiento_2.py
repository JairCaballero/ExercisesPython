lista = [11,10,12]
tupla = (11,10,12)

def func (a,b,c):
    print(a)
    print(b)
    print(c)


# lista.sort()
# func(*lista)

#desenapquetamos lso elementos de la tupla en uan lista para asi poder ordenarlos
l = [*tupla]
l.sort()
func(*l)

print("---------------------------------------------")

#la funcion zip intercala los valores, los de una lista con los de otra creando asi con dict un diccionario clave valor
#el primero con el primero y asi
func(**dict(zip(("b","a","c"),lista)))