class A:
   def __init__(self) :
      self._var = 0

   def _get_var(self) :
      print("leyend valor")
      return self._var

   def _set_var(self, x) :
      print("inscribedno valor valor")
      self._var = x

   var = property(fget = _get_var , fset =  _set_var) # <-- Propiedad que aplica el set y get de una

a = A()
a.var = 10
print(a.var)
