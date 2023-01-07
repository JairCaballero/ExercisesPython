
#es invocado por python automaticamente
#no es obligatorio crearlo
# def __init__(self): <-- self ase refernecia a si mismo

def teste(s):
   print(id(s))

class A:

   def __init__(self):
      print(id(self))


a = A()
print(id(a))

#el id viaja con la instancia
#teste(a)


