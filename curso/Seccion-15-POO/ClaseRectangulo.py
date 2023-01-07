class Rectangulo:

   def __init__(self): # <-- Cada instancia que se genera tendra y iniciara estos valores
      self.a = 0
      self.l = 0

   def area(self):
      return self.a * self.l


r1 = Rectangulo()
r2 = Rectangulo()

print(r1.a)
print(r2.a,"\n")

print(r1.area())
print(r2.area(),"\n")

r1.a = 2
r1.l = 3
print(r1.area(),"\n")

r2.a = 1
r2.l = 1
print(r2.area(),"\n")




