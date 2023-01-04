# se importa con import nombre
# para usar sus atributos del modulo es nombre.attr , esto se llama cualificaion de nombres

import math #añade el nombre pero no sus atributos

x = 0
#print(dir(math)) #asi listamos a los metodos de este

# al tenre que usar alguna constante es mejor tomarla y definirla en nuestro moduo
# asi no demora tanto tratando de importar y buscar la funcion todo el tiempo
e = math.e
pi = math.pi

print(e)
print(pi)
