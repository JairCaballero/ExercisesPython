#es malo levantar exepcioens ya que se ejecutara mas lento el codigo

def input_f (msg):
   while True:
      try:
         return float(input(msg))
      except ValueError:
         print("Intentelo nuevamente y ingrese un valor numerico")


n1 = input_f("Ingrese el valor 1 : ")
n2 = input_f("Ingrese el valor 2 : ")

try:
   print(n1/n2)
except ZeroDivisionError:
   print("Intentelo nuevamente no es posible dividir entre cero")



