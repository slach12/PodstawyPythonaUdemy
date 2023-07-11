
def policzProstokat():
    bokA= int(input("Podaj długość pierwszego boku: "))
    bokB= int(input("Podaj długość drugiego boku: "))
    print("Pole prostokąta:",bokA*bokB)

print("1 - prostokąt")
print("2 - kwadrat")
print("3 - trójkąt")
print("4 - trapez")
print("5 - koło")
figura = input("Podaj numer figury:")


if figura=="1":
    policzProstokat()
