#variables dinamicas ya que canvian segun su valor

num_int = 5
mun_dec = 7.3
val_str = "Texto"

#concatenacion
print("Este valor esta concatenado : ",num_int)
#le decimos que añadiremos un valor numerico con la i
print("Este valor esta concatenado con format : %i" %num_int)
#pasamos la variable a string
print("Este valor esta concatenado con format : " + str(num_int))
#porcenataje punto le decimos cuantos decimales queremos ver
print("Concatenando decimal : %.2f" %mun_dec)
print("Concatenando decimal 2 : " + str(mun_dec))
#para texto
print("Concatenado texto ",val_str)
print("Concatenado texto %s" %val_str)
print("Concatenado texto 3 : " + val_str)