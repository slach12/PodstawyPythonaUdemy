#len() - długość - length
#.append - dodać
#.extend - rozszerzyć
#.insert(index,co) - wstawić
#.index - indeks danego elementu
#.sort(reverse=False) - sortuj rosnąco
#max()
#min()
#.count() - ile razy coś wystąpi
#.pop - usuń ostatni element
#.remove - usuń pierwsze wystąpienie
#.clear - wyczyśćliste
#.reverse - zamień kolejność

lista1 = [54,1,-2,20,1]
lista2 = ["Arkadiusz", "Wioleta"]

print(lista1)
lista1=lista1+[4]
print(lista1)
lista1.append(4)
print(lista1)
lista1.extend([12,13,14])
print(lista1)

print(lista2)
lista2.insert(0,"Kuba")
print(lista2)

print(lista1.index(20))
print(lista1)
lista1.sort()
print(lista1)
print(max(lista1))
print(min(lista1))
print(lista1.count(1))
print(lista1)
lista1.pop()
print(lista1)
lista1.remove(1)
print(lista1)
lista1.reverse()
print(lista1)

lista1.clear()
print(lista1)
