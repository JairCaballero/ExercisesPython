#insertar al final
l = ['bbb','ccc']
l.append('ddd')
print(l)

#iinsertoe n un indice especifico
#indice , elemento
l.insert(0, 'aaa')
print(l)


#alterar
l[1] = "BBB"
print(l)


#eliminar
#esta limpia la lista
#l.clear()

#elimina el ultimo
l.pop()
print(l)

#un indice especifico
l.pop(1)
print(l)

l = ['aaa','bbb','ccc','ddd','eee','fff','ggg','hhh','iii','jjj']
print(l)
#eliminar en un intervalo donde inicia / donde termina
del(l[2:4])
print(l)

#eliminar en un intervalo donde inicia / donde termina / intervalo
l = ['aaa','bbb','ccc','ddd','eee','fff','ggg','hhh','iii','jjj']
print(l)
del(l[::2])
print(l)