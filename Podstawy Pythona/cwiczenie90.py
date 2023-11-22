import requests

webs= ["http://videokurs.pl",
       "http://videokurs.pl",
       "http://videokurs1.pl",
       "http://videokurs2.pl",
       "wp.pl",
       "https://pypi.org"
       ]

correct_webs=[]

for web in webs :
    print(web)
    try: 
        response =requests.get(web)
        print(response.status_code)
        if response.status_code == requests.codes.ok:
            correct_webs.append(web)
            #print(web + "jest poprawnym adresem strony")
    except:
        print("Nie poprawny adres strony")
    

print("Porawne adresy stron:")
for web in correct_webs:
    print(web);
