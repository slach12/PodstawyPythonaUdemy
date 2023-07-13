import figury


from enum import IntEnum

#Menu_Figury = IntEnum('Menu_Figury','Kwadrat Prostokąt Koło Trójkąt Trapez')

#Menu_Figury = IntEnum('Menu_Figury','Kwadrat, Prostokąt, Koło, Trójkąt, Trapez')

Menu_Figury = IntEnum('Menu_Figury',['Kwadrat', 'Prostokąt', 'Koło', 'Trójkąt', 'Trapez'])

#Menu_Figury = IntEnum('Menu_Figury',{'Kwadrat':21, 'Prostokąt':22, 'Koło':23, 'Trójkąt':24, 'Trapez':25})

print(Menu_Figury)
wybor = int(input("""Wybierz figurę , której pole chcesz obliczyć:
1. Kwadrat
2. Prostokąt
3. Koło
4. Trójkąt
5. Trapez """))

if (wybor == Menu_Figury.Kwadrat):
    a = float(input("Podaj bok kwadratu"))
    print("Pole kwadratu wynosi : ",figury.pole_kwadratu(a))
elif(wybor == Menu_Figury.Prostokąt):
    a = float(input("Podaj pierwszy bok prostokąta"))
    b = float(input("Podaj drugi bok prostokąta"))
    print("Pole prostokąta wynosi : ",figury.pole_prostokata(a,b))
elif (wybor == Menu_Figury.Koło):
    promien = float(input("Podaj promień koła"))
    print("Pole koła wynosi : ", figury.pole_kola(promien))
elif ( wybor == Menu_Figury.Trójkąt):
    a = float(input("Podaj bok trójkąta"))
    h = float(input("Podaj wysokość trójkąta opuszczonego na bok"))
    print("Pole trójkąta wynosi : ",figury.pole_trojkata(a,h))
elif (wybor == Menu_Figury.Trapez):
    a = float(input("Podaj pierwszą podstawę trapezu"))
    b = float(input("Podaj druga podstawę trapezu"))
    h = float(input("Podaj wysokość trapezu"))
    print("Pole trapezu wynosi : ",figury.pole_trapezu(a,b,h))
    
    
