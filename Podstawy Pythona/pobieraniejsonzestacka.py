import requests
import json
import pprint

params = {
           "site" : "stackoverflow",
           "sort" : "votes",
           "order" : "desc",
           "fromdate" : "2023-12-23",
           "tagged" : "python",
           "min" : 5
        }


r = requests.get("https://api.stackexchange.com/2.2/questions/", params)

try:
    questions = r.json()
except json.decoder.JSONDecodeError :
    print("Niepoprawny format")
else:
    pprint.pprint(questions )
