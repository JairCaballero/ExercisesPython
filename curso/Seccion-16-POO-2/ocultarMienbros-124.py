class Rectangulo:

   def __init__(self, largo, alto):
      self._largo = 0 #<-- con un _nombre evitamos que se pueda adquirir externamente
      self._alto = 0
      self.__var = 0
      #<-- para evitar colicones en herencia se ase asi, ya que internamente python asigna _nombleclase__var como nombre
      #pero para nuestro uso seguira siendo __var
      self.set_altura(alto)
      self.set_largo(largo)

   def set_altura(self, num):

      if(not(isinstance(num, int) and (num > 0))): # <-- Validar tipo de dato que llega
         raise ValueError(f"Altura Invalida : {num}")
      self._alto = num

   def set_largo(self, num):

      if(not(isinstance(num, int) and (num > 0))): # <-- Valid
         raise ValueError(f"Largo Invalida : {num}")
      self._largo = num

   def get_area(self):
      return self._alto * self._largo



r = Rectangulo();


