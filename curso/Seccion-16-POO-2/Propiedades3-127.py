# class Rectangulo:

#    def __init__(self, largo, alto):
#       self._largo = 0
#       self._alto = 0
#       self._set_altura(alto)
#       self._set_largo(largo)

#    def _get_altura(self):
#       return self._alto

#    def _get_largo(self):
#       return self._largo

#    def _set_altura(self, num):

#       if(not(isinstance(num, int) and (num > 0))):
#          raise ValueError(f"Altura Invalida : {num}")
#       self._alto = num


#    def _set_largo(self, num):

#       if(not(isinstance(num, int) and (num > 0))):
#          raise ValueError(f"Largo Invalida : {num}")
#       self._largo = num

#    def _get_area(self):
#       return self._alto * self._largo


#    altura = property(fget = _get_altura, fset = _set_altura)
#    altura = property(fget = _get_largo, fset = _set_largo)
#    area = property(fget = _get_area)


# r = Rectangulo(largo = 5 , alto = 5);
# r.largo = 10
# r.alto = 15
# r.area = 1000

# print(r.alto)
# print(r.largo)
# print(r.area)




# Con decorator que es mejor ya que es mas legible

class Rectangulo:

   def __init__(self, largo, alto):
      self._largo = 0
      self._alto = 0
      self.alto = alto
      self.largo = largo

   @property
   def alto(self):
      return self._alto

   @property
   def largo(self):
      return self._largo

   @alto.setter
   def alto(self, num):

      if(not(isinstance(num, int) and (num > 0))):
         raise ValueError(f"Altura Invalida : {num}")
      self._alto = num

   @alto.setter
   def largo(self, num):

      if(not(isinstance(num, int) and (num > 0))):
         raise ValueError(f"Largo Invalida : {num}")
      self._largo = num

   @property #solo lectura si usamos el area manda error
   def area(self):
      return self._alto * self._largo



r = Rectangulo(largo = 5 , alto = 5);
r.largo = 10
r.alto = 15
# r.area = 1000

print(r.alto)
print(r.largo)
print(r.area)