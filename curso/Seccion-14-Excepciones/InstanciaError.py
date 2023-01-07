def error (x):
   try:
      eval(x)
   except ValueError as e:
      print("ValueError")
      print(type(e))
      print(type(e.args))
      print(e)
   except (TypeError,NameError) as e :
      print("TypeError o NameError")
      print(type(e))
      print(type(e.args))
      print(e)

#typeError
error("int+int")
print ("------------------------------")

#NameError
error("a")
print ("------------------------------")

#ValueError
error("int('a')")
print ("------------------------------")