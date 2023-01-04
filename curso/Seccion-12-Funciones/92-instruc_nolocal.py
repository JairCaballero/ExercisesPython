# sirve para acceder a mienbros dentro de una funcion anidada y solo eso
# con nonlocal accedmos a valores que no estan en el ambito global ni local
# lo que nos daria solo el ambito de una fun anidada

a = 0


def func1():
    b = 0
    print(b)

    def func2():
        nonlocal b
        b = 5
        print(b)

    func2()


func1()


x = 1


def funx():
    # nonlocal x #esto nos dara error para esto se usa es global
    global x
    return x


print(funx())
