#empaqueta es cuando añade elemnetos a una estructura y desenpaquetar es sacarlos

def func(a,b):
  print(a, "y" ,b)


lista = [1,4]
func(*lista)


def persona (nombre,pais):
  print("el nombre es ",nombre)
  print("el pais es ",pais)


tupla = "marco","veneco"
persona(*tupla)
print("------------------------------")
#con dicc se pone el mismo nombre que en el argu
d = {"pais":"colombia","nombre":"jair"}
persona(**d)