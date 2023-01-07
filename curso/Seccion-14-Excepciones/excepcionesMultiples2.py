def error (x):
   try:
      eval(x) # <-- ejecuta valores a formato string para que python ejecute
   except (TypeError,NameError):
      print("TypeError o NameError")
   except ValueError:
      print("ValueError")
   except ZeroDivisionError:
      print("ZeroDivisionError")


#typeError
error("int+int")

#NameError
error("a")

#ValueError
error("int('a')")

#ZeroDivisionError
error("5/0")

error("10+10")



