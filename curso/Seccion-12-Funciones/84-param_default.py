#le asignamos un valor default para asi, sino se pasa no genre problema
#los no obligatorios deben ser los ultimos en asignarce, primero los obligatorios

def login(sistema, usuario = "root",contraseña = "123"):
  print("Welcome " + usuario + "!!")
  print("Constraseña " + contraseña + "!!")
  print("Sistema Operatibo " + sistema + "!!")


login("Windows")