"""
Program liczy sumę liczb od 1 do podanej

"""

def sumuj_do(liczba):
    suma=0
    for liczba in range(1,liczba):
        suma = suma +liczba
    return suma

def sumuj_do2(liczba):
    return sum([liczba for liczba in range(1,liczba+1)])

def sumuj_do3(liczba):
    return sum({liczba for liczba in range(1,liczba+1)})

def sumuj_do4(liczba):
    return sum((liczba for liczba in range(1,liczba+1)))


def sumuj_do5(liczba):
    return (1 + liczba )/2 * liczba

def finish_timer(start):
    end = time.perf_counter()
    return end - start



number = 1250000
start = time.perf_counter()
print(sumuj_do(number))
print(finish_timer(start))

start = time.perf_counter()
print(sumuj_do2(number))
print(finish_timer(start))

start = time.perf_counter()
print(sumuj_do3(number))
print(finish_timer(start))

start = time.perf_counter()
print(sumuj_do4(number))
print(finish_timer(start))

start = time.perf_counter()
print(sumuj_do5(number))
print(finish_timer(start))
