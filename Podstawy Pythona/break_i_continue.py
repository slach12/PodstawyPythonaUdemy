"""
break

contiune
"""
"""

wynik =0

while i < 3:
    x = int(input("Podaj dodatnią liczbę : "))
    if(x>0):
        wynik+=x
    else:
        print("Miała być liczba dodatnia kończymy za karę!")

    print("Aktualny wynik dodawania to : ",wynik)
    i+=1
"""    

wynik =0
i=0
while i < 3:
    x = int(input("Podaj dodatnią liczbę parzystą : "))
    if(x<=0):
        print("Miała być liczba dodatnia.")
        continue
    if (x%2 !=0):
        print("Miała być liczba parzysta.")
        continue
    wynik+=x    
    print("Aktualny wynik dodawania to : ",wynik)
    i+=1
print("Końcowy wynik dodawania to : ",wynik)


