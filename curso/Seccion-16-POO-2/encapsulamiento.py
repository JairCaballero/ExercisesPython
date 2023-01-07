class Rectangulo:

   def __init__(self,largo,alto):
      self.l = largo
      self.a = alto

   def area(self):
      return self.l * self.a



r = Rectangulo(10,5)
r.l = "teste" # <-- aceder a un objeto interno puede pasar y no debe
print(r.area())
