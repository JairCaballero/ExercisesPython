
class Rectangulo:

   def __init__(self,largo,alto):
      self.l = largo
      self.a = alto

   def area(self):
      return self.l * self.a

#pasandole los atributos directamente, serian obligatorios ya que los pusimos hay
r = Rectangulo(7,5);

print(r.area())


