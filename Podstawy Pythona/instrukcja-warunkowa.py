"""
INSTURKCJA WARUNKOWA

JEŚLI (PRAWDA)
 TO...
JEŚLI CO INNEGO (PRAWDA)
 TO...
A CAŁKOWICIE W INNYM WYPADKU
"""

if(5<3):
    print("lalal")
    print("tralala")
"""
a = int(input())
b = int(input())

if(a>b):
    print("a jest większy od b")
elif (b>a):
    print("b jest większy od a")
else:
    print("a jest równe b")

"""

wybor = input("* - mnożenie, / - dzielić, + - dodawać, - - odejmować, ^ - potęgowanie, % - modulo")

a = int(input("Podaj liczbę a :"))
b = int(input("Podaj liczbę b :"))

if (wybor=="*"):
    print(a*b)
elif(wybor=="/"):
    if(b==0):
        print("Cholero nie dziel przez zero")
    else:
        print(a/b)
elif(wybor=="+"):
    print(a+b)
elif(wybor=="-"):
    print(a-b)
elif(wybor=="^"):
    print(a**b)
elif(wybor=="%"):
    print(a%b)
else:
    print("Nie wybrałeś dobrego wyboru")
