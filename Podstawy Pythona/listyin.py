imiona = ["Arkadiusz","Wioleta","Karol","Kuba","Adrian"]
liczby =[1,54,-2,20]

print("Arkadiusz" in imiona)
imiona[-1]="Wojtek"
if("Wojtek" in imiona):
    print("Cześć Wojtku")

if(2 not in liczby):
    print("Nie ma liczby 2")
else:
    print("Liczba 2 jest w liście")


print(3*liczby)
print([4]+ liczby)
