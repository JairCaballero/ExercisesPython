s = "Texto con doble"

#podemos aser un obj con un indice ya que enumerate los añade dinamicamente
dic = dict(enumerate("testo"))
print(dic)


for k,v in enumerate("texto"):
    print(k,v)