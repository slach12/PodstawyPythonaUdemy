pokoje = {49:"Arkadiusz",69:"Żona"}

print(pokoje[49])
pokoje[50] = 'Ksawery'

print(pokoje[50])
imiona={"imie" : "Sławek","nazwisko":"Łach"}
print(imiona["imie"])
print(pokoje.get(49))
pokoje.update({2:'2',3:'3'})
print(pokoje)
del(pokoje[2])
print(pokoje)
print(pokoje.pop(3))
print(pokoje)
print(pokoje.popitem())
print(len(pokoje))
