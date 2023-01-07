# cuandos se ejecuta un return toda funcion se corta
def suma(x, y):
    num = x+y
    return num


print(suma(20, 3))


def func():
    return 1, 2


def func_2(n1, n2):
    return n1, n2


# esto es llamdao desenpaquetamiento o asignarle a 2 var lo contenido en 1 var
a, b = func()
print(a, " y ", b)

a1, b1 = func_2(3, 6)
print(a1, " y ", b1)

# esto es llamdao desenpaquetamiento
t = (10, 20)
c, d = t
print(t)