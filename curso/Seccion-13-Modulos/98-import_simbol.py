# from modulo import simbolo, simbolo2 ....
# import modulo as nombre
# as para darle un nombre especificado
# from modulo import simbolo as s, simbolo2 as s2....
#tambien podemos import todo con from modulo import * pero esto es malo

from math import pi, e
from math import sqrt

print(pi)
print(e)
print(sqrt(9))


def func():
    from math import factorial #<-- Solo funcionara en esta funcion local
    print(factorial(10))


func()





