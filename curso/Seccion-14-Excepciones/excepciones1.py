
#añadirmos en try el codigo que puede generar el eror
#excep es para el mensaje o accion que se ejecutara dependiendo del error

try:
   a = 10 / 0
except ZeroDivisionError:
   print ("No es posible dividir entre cero")

