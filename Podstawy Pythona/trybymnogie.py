

with open("oceany.txt","a+",encoding="UTF-8") as file:
          file.write("Ocean Arka")
          print(file.tell())
          file.seek(0)
          print(file.readline())
          print(file.tell())
          file.write("Ocean Arkadiusza Wielkiego")
          
