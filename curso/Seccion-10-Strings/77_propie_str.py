s = "Texto con doble"
print(len(s))
print(s[3])

#alterar string
s2 = s.split(" ")

s3 = s2[0] + " " + s2[2]
print(s3)

#mejor asi
s.replace("con","nuevo")
print(s)