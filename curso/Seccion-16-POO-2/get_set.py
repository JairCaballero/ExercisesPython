# get <-- retorna el valor
# set <-- reciben valores para editar un mienbro
# isinstance (valor,tipo de dato que quiere validar) <-- que el valor sea == al tipo de dato sino retorna false

class Rectangulo:

   def __init__(self, largo, alto):
      self.largo = 0
      self.alto = 0
      self.set_altura(alto)
      self.set_largo(largo)

   def set_altura(self, num):

      if(not(isinstance(num, int) and (num > 0))): # <-- Validar tipo de dato que llega
         raise ValueError(f"Altura Invalida : {num}")
      self.alto = num

   def set_largo(self, num):

      if(not(isinstance(num, int) and (num > 0))): # <-- Valid
         raise ValueError(f"Largo Invalida : {num}")
      self.largo = num

   def get_area(self):
      return self.alto * self.largo


#r = Rectangulo(largo = 10, alto = 5)
#print(r.get_area())

r = Rectangulo(largo = 10, alto = "f")