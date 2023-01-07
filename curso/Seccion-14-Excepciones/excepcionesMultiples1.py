def error (x):
   try:
      eval(x) # <-- ejecuta valores a formato string para que python ejecute
   except TypeError:
      print("TypeError")
   except NameError:
      print("NameError")
   except ValueError:
      print("ValueError")
   except ZeroDivisionError:
      print("ZeroDivisionError")


#typeError
error("int+int")

#NameError <-- nombre no definido
error("a")

#ValueError
error("int('a')")

#ZeroDivisionError
error("5/0")

error("10+10")


