# usar decorator para definir propiedades
# es mejor que la funcion building properti pq ase dificil la lectura del codigo

# el nombre de la funcion deve llamarce igual que el del propiedad a usar

class A:
   def __init__(self) :
      self._var = 0

   @property # <-- metodo encargado de retornar el valor cuando var este siendo leido
   def var(self) :
      return self._var

   @var.setter  # <-- metodo encargado de definir el valor cuando var este siendo escrito
   def var(self, x) :
      self._var = x


a = A()
a.var = 10 # <-- atribuye osea get
t = a.var # <-- leee osea set
print(t)





