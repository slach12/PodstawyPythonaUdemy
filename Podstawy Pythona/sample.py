

imiona =["Arkadiusz","Wiola","Antek"]

print("Kim jesteś?")
imie = input()
imie = imie.capitalize()

"""
if imie in imiona:
    print("Masz dostęp")
else:
    print("Brak dostępu")
"""

if imie =="Arkadiusz" or imie == "Wiola" or imie =="Antek":
    print("Masz dostęp")
else:
    print("Brak dostępu")
