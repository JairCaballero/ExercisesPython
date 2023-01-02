tel = {}
tel = {}
tel = {
    123456789 : "jair",
    987654321 : "Febro",
    246809753 : "Febro"
}

#cantidad e elementos
print(len(tel))
print("-----------------------------------------")

#del ppara elimianr
print(tel)
del(tel[246809753])
print(tel)
print("-----------------------------------------")

#lista llaves
print(tel.keys())
print("-----------------------------------------")

#lista de valores
print(tel.values())
print("-----------------------------------------")

#obtener el valor tambien asi
print(tel[123456789])
print(tel.get(123456789))
print("-----------------------------------------")

#retorna y remueve un elemento
print(tel.popitem())
print(tel)
print("-----------------------------------------")

#saver si hay algo en el dict
tel = {
    123456789 : "jair",
    987654321 : "Febro",
    246809753 : "Febro"
}

print(123456789 in tel)
print(1234567890 in tel)
print("-----------------------------------------")

#mesclar dict
tel2 = {9999999 :"JAIR2",8888888:"FEBRO2"}
tel.update(tel2)
print(tel)
print("-----------------------------------------")

#poner otras cosas como llaves (no se puede con listas)
t= (10,10,10)
tel[t] = "llave como tupla"
print(tel)