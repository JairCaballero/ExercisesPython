edad = int(input("Digite su edad: "))

if(edad <= 0):
    print("Su edad no puede ser 0 o menor a 0")
elif(edad>150):
    print("Su edad no puede ser mayor a 150")
elif(edad<18):
    print("Usted nececita ser mayor de edad")
else:
    print("Usted es mayor de edad, todo correcto")