ratings1 = {
                   "Arkadiusz": (2,1,2,3,2,3),
                   "Agnieszka": (4,2,1,3,4)
                 }



people3 = [ 
            "Arkadiusz",
            "Wiola",
            "Kuba"
          ]

people2 = [
         {'id': 'IcFDG2bO9AYDF651DoyH', 'name': 'John', 'age': 27, 'sex': 'Male'},
         {'id': 'KcD9ntE6IRM59vkVta1k', 'name': 'Marie', 'age': 22, 'sex': 'Female'},
         {'id': 'yDlgcn99xPc19mYXcRmy', 'name': 'Agness', 'age': 25, 'sex': 'Female'}               
          ]

people = {
        "IcFDG2bO9AYDF651DoyH": {'name': 'John', 'age': 27, 'sex': 'Male'},
        "KcD9ntE6IRM59vkVta1k": {'name': 'Marie', 'age': 22, 'sex': 'Female'},
        "yDlgcn99xPc19mYXcRmy": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
        "cpQh6GiAbBdGv35NDoTk": {'name': 'Nabeel', 'age': 17, 'sex': 'Male'},
        "12BifzWxCQySKgLhgahC": {'name': 'Jasmin ', 'age': 42, 'sex': 'Female'},
        "QLnmg0pzlLj9x7c7DlLv": {'name': 'Ruby', 'age': 55, 'sex': 'Female'},
        "To47urX0DUznWmOxGZ6H": {'name': 'Lori', 'age': 27, 'sex': 'Male'},
        "KQ4bir3y4tlkbG69I7zq": {'name': 'Marie', 'age': 42, 'sex': 'Female'},
        "94cp4hsyZP2BnCh4D34z": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
        "Vr4wRdkljeEs46Czxo54": {'name': 'Chiara', 'age': 17, 'sex': 'Male'},          
         }



#print(ratings1["Arkadiusz"])
#print(ratings1["Agnieszka"])
"""
for key in ratings1:
    print(key,"oceny",ratings1[key])


for recod in people2:
    for key in recod:
        print(key,":",recod[key])

print(people["IcFDG2bO9AYDF651DoyH"])

for key in people:
    print("Id : ",key)
    for secendarykey in people[key]:
        print(secendarykey," : " ,people[key][secendarykey])

"""


print(people.items())
for id,dictionary in people.items():
    for key in dictionary:
        print(key,":",dictionary[key])
