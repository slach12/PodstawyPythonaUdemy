import requests
import json
from pprint import pprint
import webbrowser
from datetime import datetime, timedelta
import credentials as cr

#print(datetime.today())
#print(timedelta(days=7))

timeBefore = timedelta(days =10)
searchDate = datetime.today() - timeBefore


'''
params = {
           "api_key" : "mUKzVG9C1VNMHZ1TqmG9eF6oPsC20Vgx",
           "country" : "pl",
           "year" : 2023,
           "month" : 12
        }
'''



r = requests.get("https://api.thecatapi.com/v1/favourites", headers= cr.headers)






try:
    content = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
     pprint(content)


print(content)
