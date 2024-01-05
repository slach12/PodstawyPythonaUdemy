import requests
import json
import pprint
import webbrowser
from datetime import datetime, timedelta


#print(datetime.today())
#print(timedelta(days=7))

timeBefore = timedelta(days =10)
searchDate = datetime.today() - timeBefore


params = {
           "amount" : 5,
           "animal_type" : "dog"
          
        }


r = requests.get("https://cat-fact.herokuapp.com/facts/random", params)






try:
    content = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    for cat in content:
        print(cat["text"])
        print("--------------");
