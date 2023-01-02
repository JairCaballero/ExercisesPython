# `1) Realice un algoritmo que lea un número y muestre si el mismo es positivo, negativo o cero.
print("---------------------------------1-----------------------------")
numero = int(input("Ingrese el numero: "))
if(numero < 0):
    print("Numeo negativo")
elif(numero > 0):
    print("Número positivo")
elif(numero == 0):
    print("Numero iguala a 0")

# 2) Realice un algoritmo que lea un número y muestre si el mismo es par o ímpar.
print("---------------------------------2-----------------------------")
numero = int(input("Ingrese el numero: "))
if((numero%2) == 0):
    print("Numeo par")
elif((numero%2) != 0):
    print("Número impar")

# 3) Realice un algoritmo que lea a dos números e imprima al mayor de ellos.
print("---------------------------------3-----------------------------")
num1 = int(input("Ingrese el num1: "))
num2 = int(input("Ingrese el num2: "))
if(num1 > num2):
    print("El nuemro1 es mayor que el nuemro2")
else:
    print("El nuemro2 es mayor que el nuemro1")

# 4) Realice un algoritmo que pida la edad de una persona e imprima en la pantalla si la misma es mayor de edad o menor de edad.
print("---------------------------------4-----------------------------")
edad = int(input("Digite su edad: "))
if(edad<18):
    print("Usted nececita ser mayor de edad")
else:
    print("Usted es mayor de edad, todo correcto")

# 5) Realice un algoritmo que pida la edad del usuario y la edad de su madre. Seguidamente, imprima en la pantalla la edad a la que su mamá lo tuvo.
print("---------------------------------5-----------------------------")
edad_hijo = int(input("Digite su edad: "))
edad_madre = int(input("Digite la edad de su mama: "))
tubo = edad_madre-edad_hijo
print("Tu madre te tubo a la edad de",tubo)

# 6) Realice un algoritmo que imprima 50 veces el carácter "-" en la pantalla (sin la utilización de bucles de repetición).
print("---------------------------------6-----------------------------")
guion = 50*"-"
print(guion)

# 7) Realice un algoritmo que pida un número al usuario y verifique si el mismo es par o impar.
print("---------------------------------7-----------------------------")
numero = int(input("Ingrese el numero: "))
if((numero%2) == 0):
    print("Numeo par")
elif((numero%2) != 0):
    print("Número impar")

# 8) Realice un algoritmo que pida dos números. Primero, imprima al mayor de ellos y, seguidamente imprima al menor de ellos.
print("---------------------------------8-----------------------------")
num1 = int(input("Ingrese el num1: "))
num2 = int(input("Ingrese el num2: "))
if(num1 > num2):
    print("Mayor : ",num1)
    print("Menor : ",num2)
if(num1 < num2):
    print("Mayor : ",num2)
    print("Menor : ",num1)

# 9) Realice un algoritmo que verifique si un determinado valor es un número entero.
print("---------------------------------9-----------------------------")
numero = int(input("Ingrese el numero: "))
if(type(numero) == int):
    print("Numeo entero")
else:
    print("Número no entero")

# 10) Realice un algoritmo que verifique si un determinado valor es una String.
print("---------------------------------10-----------------------------")
valor = 1
if(type(valor) == str):
    print("El valor ingrsado es un string")
else:
    print("El valor ingresado no es un string")

# 11) Realice un algoritmo que verifique si un determinado valor es de tipo decimal.
print("--------------------------------11-----------------------------")
valor = 1.222
if(type(valor) == float):
    print("el valro ingresado es decimal")
else:
    print("El valor ingresado no es decimal")

# 12) Realice un algoritmo que pida un valor numérico. Seguidamente, verifique si el número es entero o decimal.
print("---------------------------------12-----------------------------")
numero = int(input("Ingrese el numero: "))
if(type(numero) == int):
    print("Numeo entero")
elif(type(numero_2) == float):
    print("Número deciaml")

# 13) Realice un algoritmo que lea tres números e imprima en la pantalla al mayor de ellos.
print("---------------------------------13-----------------------------")
num1 = int(input("Ingrese el num1: "))
num2 = int(input("Ingrese el num2: "))
num3 = int(input("Ingrese el num3: "))

if((num1 > num2 > num3) ):
    print("Mayor : ",num1)
if((num2 > num1 > num3) ):
    print("Mayor : ",num2)
else:
    print("Mayor : ",num3)

# 14) Realice un algoritmo que lea tres números e imprímalos en orden creciente.
print("--------------------------------14-----------------------------")
num1 = int(input("Ingrese el num1: "))
num2 = int(input("Ingrese el num2: "))
num3 = int(input("Ingrese el num3: "))

if((num1 > num2 > num3) ):
    print("orden : ",num1," ",num2," ",num3)
if((num1 > num3 > num2) ):
    print("orden : ",num1," ",num3," ",num2)

if((num2 > num1 > num3) ):
    print("orden : ",num2," ",num1," ",num3)
if((num2 > num3 > num1) ):
    print("orden : ",num2," ",num3," ",num1)

if((num3 > num2 > num1) ):
    print("orden : ",num3," ",num2," ",num1)
if((num3 > num1 > num2) ):
    print("orden : ",num3," ",num1," ",num2)

# 15) Realice un algoritmo que lea un caracter e informe si el mismo es una vocal o no.
print("--------------------------------15-----------------------------")
caracter = input("Ingrese el caracter: ")

if(caracter == "a" or caracter == "e" or caracter == "i" or caracter == "o" or caracter == "u"):
    print("El caracter ingresado es una vocal")
else:
    print("El caracter ingresado no es una vocal")

# 16) Las direcciones de IP versión 4 son divididas en cinco clases: A, B, C, D y E. Las direcciones  que se encuentran en un intervalo
# entre 0 y 127 pertenecen a la clase A, entre 128 y 191 pertenecen a la clase B, entre 192 y 223 pertenecen a la clase C, entre 224 y 239
# pertenecen a la clase D y a partir de 240 pertenecen a la clase E. Realice un algoritmo que lea el primer octeto, en el formato decimal
# de una dirección IP, e informe su clase.
print("---------------------------------16-----------------------------")
ip = input("Ingrese el IP: ")
#no entendi la pregunta

# 17) Realice un algoritmo que reciba un número entero, que represente un determinado mes del año, y que muestre el mes correspondiente.
# Por ejemplo, si es informado el número 2, el algoritmo deberá exhibir: febrero. El algoritmo también debe validar si la entrada es correcta.
print("---------------------------------17-----------------------------")
mes = int(input("Ingrese un mes en numero: "))
if(mes ==1):
    print("El mes es enero")
elif(mes ==2):
    print("El mes es febrero")
elif(mes ==3):
    print("El mes es marzo")
elif(mes ==4):
    print("El mes es abril")
elif(mes ==5):
    print("El mes es mayo")
elif(mes ==6):
    print("El mes es julio")
elif(mes ==7):
    print("El mes es junio")
elif(mes ==8):
    print("El mes es agosto")
elif(mes ==9):
    print("El mes es septiembre")
elif(mes ==10):
    print("El mes es octubre")
elif(mes ==11):
    print("El mes es noviembre")
elif(mes ==12):
    print("El mes es diciembre")
else:
    print("ese emsno exite")

# 18) Realice un algoritmo que valide una fecha. La misma debe estar constituída por dia, mes y año. Por ejemplo, si el usuario escribe la
# fecha 10/8 la misma será inválida. Y en caso de que el usuario  escriba la fecha 01/10/2018, la misma debe ser considerada válida.`
print("---------------------------------18-----------------------------")
fecha = input("Digite una fecha en este formato d/m/a: ")
#asta este putno no se puede, pq nececito libreria
