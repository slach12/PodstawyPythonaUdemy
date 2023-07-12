import math
def policzProstokat():
    bokA = int(input("Podaj długość pierwszego boku: "))
    bokB = int(input("Podaj długość drugiego boku: "))
    pole = bokA * bokB
    print("Pole prostokąta:",pole)

def policzKwadrat():
    bokA= int(input("Podaj długość boku: "))
    pole = bokA * bokA
    print("Pole kwadratu :",pole)

def policzTrojkat():
    bokA = int(input("Podaj długość boku: "))
    wysokosc = int(input("Podaj długość wysokości opuszczonej na ten bok: "))
    pole = wysokosc * bokA *0.5
    print("Pole trójkąta :",pole)

def policzTrapez():
    bokA = int(input("Podaj długość pierwszej podstawy: "))
    bokB = int(input("Podaj długość drugiej podstawy: "))
    wysokosc = int(input("Podaj długość wysokości: "))
    pole = (bokA + bokB) * wysokosc * 0.5
    print("Pole trapezu :",pole)

def policzKolo():
    promien= int(input("Podaj długość promienia: "))
    pole = promien**2 * math.pi
    print("Pole kola :",pole)

    
print("1 - prostokąt")
print("2 - kwadrat")
print("3 - trójkąt")
print("4 - trapez")
print("5 - koło")
figura = input("Podaj numer figury:")


if figura=="1":
    policzProstokat()
elif figura == "2":
    policzKwadrat()
elif figura == "3":
    policzTrojkat()
elif figura == "4":
    policzTrapez()
elif figura == "5":
    policzKolo()
else:
    print("Wybrałeś nie właściwą liczbę.")


