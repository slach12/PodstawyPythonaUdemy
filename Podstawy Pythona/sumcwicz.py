def sumujDodatnieLiczby(liczby):
    suma = 0
    for liczba in liczby:
        if liczba> 0:
            suma = suma + liczba
    return suma

liczby = [1,2,3,4,5,6]
print(sumujDodatnieLiczby(liczby))
