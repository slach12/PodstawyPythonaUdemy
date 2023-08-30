
with open("oceany.txt","r",encoding="UTF-8") as file:
    #oceany = file.read().splitlines()
    oceany = file.read()
    


print("Oceany")
print(oceany)

print("Drugie wczytanie")
with open("oceany.txt","r",encoding="UTF-8") as file:
    for line in file:
        print(line)
