a = 10
b = 25
c = 66

x = int(input("Ingres un nuemro : "))

# if(x == a or x == b or x == c):
#     print("Esta contenido")
# else:
#     print("No contenido")


if(x in [a,b,c]):
    print("Esta contenido")
else:
    print("No contenido")