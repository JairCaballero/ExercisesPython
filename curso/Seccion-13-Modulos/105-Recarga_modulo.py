#como recargar modulos en tiempo de ejecucion
# cuando se importa este cargara y eejcutara 1 sola ves la importacion durante toda el ciclo del codigo
#recargar modulos es mala practica ya que redefinira todo

import importlib
import simbolosPublic.herramientas as herra


print(herra.aa)
herra.aa = 100
print(herra.aa)

#borrarlos de la tabla de simbolo
del(herra.aa)
#print(herra.aa)

#importlib.reload(simbolosPublic.herramientas)
#despues de reinportarlos los valores de las variables se reinician a como estaban en el modulo importado


