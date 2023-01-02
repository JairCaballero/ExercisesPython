print("---------------------------------1-----------------------------")

'''
1) Realice un algoritmo que imprima solamente su nombre en la pantalla
y seguidamente finalice la aplicación.
'''
print("Mi nombre es: Dwan jair pimiento caballero")


print("---------------------------------2-----------------------------")
'''
2) Realice un algoritmo que solicite al usuario que escriba su nombre
y seguidamente envíe la siguiente frase a la salida estándar:"Su nombre es: [nombre del usuario]".
'''
nombre = str(input("Ingrese el nombre: "))
print("Mi nombre es: "+nombre)


print("---------------------------------3-----------------------------")
'''
3) Realice un algoritmo que solicite el nombre y la edad del usuario.,
seguidamente, envíe la siguiente frase a la consola: "El nombre es <nombre> y su edad es <edad>"
'''
nombre = str(input("Ingrese el nombre: "))
edad = str(input("Ingrese el edad: "))

print("El nombre es "+nombre+" y su edad es "+edad)


print("---------------------------------4-----------------------------")
'''
4) Realice un algoritmo que solicite al usuario informar un número. Seguidamente,
almacene a este número en una variable. Por último, envíe a ese número a la salida estándar.
'''
numero = int(input("Ingrese el numero: "))
print(numero)


print("---------------------------------5-----------------------------")
'''
5) Realice un algoritmo que solicite al usuario informar un número. Seguidamente, escriba
el siguiente mensaje  "El número escrito fue:   "
'''
numero = int(input("Ingrese el numero: "))
print("El numero escrito fue: ",numero)


print("---------------------------------6-----------------------------")
'''
6) Realice un algoritmo que solicite al usuario informar 3 números. Seguidamente,
sume los valores y envíe a la salida estándar la siguiente frase "La suma total es:  ".
'''
num1 = int(input("Ingrese el numero 1: "))
num2 = int(input("Ingrese el numero 2: "))
num3 = int(input("Ingrese el numero 3: "))
print("la suma total es: ", num1+num2+num3)


print("---------------------------------7-----------------------------")
'''
7) Realice un algoritmo que solicite al usuario informar 2 números. Seguidamente,
sume los valores y envíe a la salida estándar la siguiente frase: "La suma entre <X> e <Y> es igual a <total>"
'''
num1 = int(input("Ingrese el numero 1: "))
num2 = int(input("Ingrese el numero 2: "))
print("la suma entre ",num1," y ",num2," es igual a ",num1+num2)


print("---------------------------------8-----------------------------")
'''
8) Realice un algoritmo que solicite las notas de las 4 pruebas semestrales al usuario.
Seguidamente, calcule la media y envíe el valor resultante a la salida estándar:
'''
nota1 = int(input("Ingrese el numero 1: "))
nota2 = int(input("Ingrese el numero 2: "))
nota3 = int(input("Ingrese el numero 3: "))
nota4 = int(input("Ingrese el numero 4: "))
media = nota1+nota2+nota3+nota4 / 4
print("La media es igual a ",media)


print("---------------------------------9-----------------------------")
'''
9) Realice un algoritmo que solicite al usuario que informe una medida en metros
Seguidamente, convierta a esta medida de metros a centímetros y envíela a la salida estándar.
'''
metros = int(input("Ingrese una medida en metros: "))
centimetros = metros/(100/1)
print("La centímetros es igual a ",centimetros)


print("--------------------------------10-----------------------------")
'''
10) Realice un algoritmo que calcule el cubo y el cuadrado de un determinado número:
'''
numero = int(input("Ingrese el numero: "))
cubo = numero**3
cuadrado = numero**2
print("el cubo es igual a ",cubo)
print("el cuadrado es igual a ",cuadrado)


print("--------------------------------11-----------------------------")
'''
11) Realice un algoritmo que solicite al usuario que escriba 2 números. Seguidamente,
imprima el total de la división en números  decimales y el total de la división en números
enteros ( es decir, sin casillas decimales).
'''
numero1 = int(input("Ingrese el numero1: "))
numero2 = int(input("Ingrese el numero2: "))
d_decimal = numero1/numero2
d_entera = numero1//numero2
print("la divicion entera es ",d_entera)
print("la divida decimal es ",d_decimal)


print("--------------------------------12-----------------------------")
'''
12) Realice un algoritmo que solicite al usuario la longitud y la altura de un cuadrado.
Seguidamente, imprima para el usuario cuántos metros cuadrados posee el área total del cuadrado.
'''
longitud = int(input("Ingrese el longitud: "))
altura = int(input("Ingrese el altura: "))



print("--------------------------------13-----------------------------")
'''
13) Realice un algoritmo que solicite al usuario informar una cantidad de días, horas, minutos
y segundos. Seguidamente, convierta todo a segundos.
'''
horas = int(input("Ingrese el horas: "))
minutos = int(input("Ingrese el minutos: "))
segundos = int(input("Ingrese el segundos: "))
total_s = (horas(3600/1))+(minutos(60/1))+segundos

print("Los valores ingresados en segundos es :",total_s)


print("--------------------------------14-----------------------------")
'''
14) Realice un algoritmo que solicite al usuario informar el valor de una compra.Seguidamente,
aplique un 10% de descuento e imprima en la pantalla tanto el valor total como el valor con el descuento aplicado.
'''
compra = int(input("Ingrese el compara: "))
descuento = compra-((10/100)*compra)
print("El descuento es :",descuento)


