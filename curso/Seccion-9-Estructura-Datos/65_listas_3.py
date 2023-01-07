#añadir
lista = [1,2,3,4,5]
lista = lista + [6,7]
lista = [0] + lista
print(lista)

lista.append(8)
print(lista)

lista.append([0])
print(lista)

lista2 = 10*[0]
print(lista2)

#eliminar
del(lista[-1])
print(lista)

#saber el mayor de una lista copn max(lista) o minimo con min(lista)

