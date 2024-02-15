import requests
import json
import pprint
import webbrowser
import credentials
from datetime import datetime, timedelta


#print(datetime.today())
#print(timedelta(days=7))

timeBefore = timedelta(days =10)
searchDate = datetime.today() - timeBefore

'''
params = {
           "amount" : 5,
           "animal_type" : "dog"
          
        }
'''

def get_json_from_response(response):
    try:
        content = response.json()
    except json.decoder.JSONDecodeError:
        print("Niepoprawny format", response.text)
    else:
        return content
    

def get_favourite_cats(userId):
    params = {
        "sub_id" : userId
        }
    
    r = requests.get('https://api.thecatapi.com/vl/favourites',
                     params, headers= credentials. headers)
    return get_json_from_response(r)








print("Hej, zaloguj się - podaj login i hasło")
userId = "agha2m"
name="Arkadiusz"
print("Wiaj"+name)
favouriteCats = get_favourite_cats(userId)
print("Twoje ulubione kotki to",favouriteCats)
