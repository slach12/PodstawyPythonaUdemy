

definicje = {}

def AddDefinition():
    klucz = input("Podaj klucz (słowo) do zdefiniowania: ")
    definicja = input("Podaj definicję: ")
    definicje[klucz] =definicja
    print("Definicja dodana pomyślnie.")

def FindDefinition():
    klucz = input("Czego szukasz ? : ")
    if klucz in definicje:
        print(definicje[klucz])
    else:
        print("Nie znaleziono definicji o nazwie: ",klucz)

def DeleteDefinition():
    klucz = input("Jaką definicję chcesz usunąć? : ");
    if klucz in definicje:
        del definicje[klucz]
        print("Usunięto defincję o nazwie:", klucz)
    else:
        print("Nie znaleziono definicji o nazwie", klucz)

def EndingProgram():
    print("No to pa !")
  
    



while(True):
    print("1 : Dodaj definicję")
    print("2 : Znajdź definicję")
    print("3 : Usuń definicję")
    print("4 : Zakończ")


    wybor = input("Co chcesz zrobić?")


    if (wybor == "1"):
        AddDefinition()
        
    elif (wybor =="2"):
        FindDefinition()
    elif (wybor =="3"):
        DeleteDefinition()
    elif(wybor =="4"):
        EndingProgram()
        break
    else:
        print("Wybrano spoza listy!")
        
