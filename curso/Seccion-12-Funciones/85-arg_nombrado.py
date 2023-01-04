# arg pocicionados = los arg se encuentran en el orden que se les asigno
# arg nombrado = asociamos el nombre del apram a un valor
def datos_pass(nombre, edad, sexo):
    print("Nombre : {}\nEdad : {}\nSexo : {}".format(nombre, edad, sexo))


datos_pass("Jose", 19, "M")
datos_pass(edad=24, nombre="Jair", sexo="M")
