#Typy zagnieżdzone

imie = "Arkadiusz"
wiek = 29
plec = "mężczyzna"

imie2 = "Wioletta"
wiek2 = 23
plec = "kobieta"

osoba1 = ['Arkadiusz',29,"mężczyzna"]
osoba2 = ['Wioleta',23,"kobieta"]
osoba3 = ['Kuba',33,"mężczyzna"]

listaGosci = [
            ['Arkadiusz',29,"mężczyzna"],
            ['Wioleta',23,"kobieta"],
            ['Kuba',33,"mężczyzna"],
            ]

listaGosci[0][1]= 128

print(listaGosci)

listaGosci2 = [
            ('Arkadiusz',29,"mężczyzna"),
            ('Wioleta',23,"kobieta"),
            ('Kuba',33,"mężczyzna"),
            ]


listaGosci2.append(("Karol", 25,"mężczyzna"))
print(listaGosci2)

listaGosci3 = {
            ('Arkadiusz',29,"mężczyzna"),
            ('Wioleta',23,"kobieta"),
            ('Kuba',33,"mężczyzna"),
            }

listaGosci4 = {
            ('Arkadiusz',29,"mężczyzna","234567890"),
            ('Wioleta',23,"kobieta","112233445"),
            ('AAAA',33,"mężczyzna","998877655"),
            }


listaGosci3.add(("Karol", 25,"mężczyzna"))
print(listaGosci3)



listaGosci5 = listaGosci3 | listaGosci4

print('listaGosci5')
print(listaGosci5)

for imie,wiek, plec, telefon in listaGosci4:
    print("Imię : ",imie)
    print("Wiek : ",wiek)
    print("Płeć : ",plec)
    print("Numer telefonu :",telefon)
    print("\n")


