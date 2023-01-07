#l bloque else solo se ejecuta cuando no hay errores
#si hay execion ejecurata el excep y saltara el else

def error (x):

   try:
      eval(x)
   except ValueError as e:
      print(type(e))
   except (TypeError,NameError) as e :
      print(type(e))
   else:
      print('No se jecuto nunguna exepcion')

#typeError
error("int+int")
print ("------------------------------")

#NameError
error("a")
print ("------------------------------")

#ValueError
error("int('a')")
print ("------------------------------")

error("10+10")
print ("------------------------------")