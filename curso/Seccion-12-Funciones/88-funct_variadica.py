#que reciben n parametros
#todo parametro definido con * recibira una lista
#con ** recibira un diccionario

#usar arg para listas
def list_arg (*args):
  print(args)


list_arg(12,3,4,5,6,7,8,9)

#usar kwargs para dicc
def list_arg_aso (**kwargs):
  print(kwargs)


list_arg_aso(a=1,b=2,c=3)

#primero listas y luego dicc obligatoriamente
def argunmentos(*args, **kwargs):
  print(args)
  print(kwargs)

argunmentos(1,2,3,4,uno =1, dos = 2, tres = 3)


