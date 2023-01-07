
#  Crear Metodos / atributos <-- obj.mtodo = func
#  Llamar al Metodo <-- obj.metodo()

class Rectangulo:

   def area(self):
      return self.a * self.l

#definimos el cosntructor aparte
def mienbros_rec(r):
   r.a = 0
   r.l = 0

r1 = Rectangulo()
mienbros_rec(r1)

r1.a = 2
r1.l = 3
print(r1.area())


