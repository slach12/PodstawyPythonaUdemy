def wiadomosc_powitalna(imie):
    print("Cześć",imie,",miło mi powitać Cię w moim programie.")

'''
wiadomosc_powitalna("Sławek")
wiadomosc_powitalna("Arku")
wiadomosc_powitalna("Wiolu")
wiadomosc_powitalna("Bartku")
'''

imiona = ["Sławek","Arku","Wiolu","Bartku"]
for imie in imiona:
    wiadomosc_powitalna(imie)
