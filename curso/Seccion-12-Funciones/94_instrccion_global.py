num = 10
print(num)

# retorna las variables globales o ambito de modulo
print(globals())


def func():
    x = 10
    print(x)
    # variables locales
    print(locals())
    num = 20
    print(num)


func()

print(num)
# como se ve nosotros podemos acceder a variables globales y alterarlas desde un local o fun
# pero esta no altera la variable global de la misma amenos que se le especifique

print("------------------------------------------")
b = 10


def f_num():
    global b
    b = 20
    print(b)
    #tambien se puede usar para declarar variables en el ambito global
    global var_g
    var_g = 30
    print(var_g)


f_num()
#la variable se llama despues de que la funcion la cree sino mandara error
print(var_g)

# como se ve asi si afecta a la variable o objeto global
print(b)
f_num()
print(b)


