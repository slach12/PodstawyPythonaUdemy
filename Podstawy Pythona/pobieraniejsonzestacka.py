import requests
import json
import pprint

params = {
           "site" : "stackoverflow",
           "sort" : "votes",
           "order" : "desc",
           "fromdate" : "2023-12-23",
           "tagged" : "python"
           "min" : 15
        }


r = requests.get("https://api.stackexchange.com/2.2/questions/", params)

try:
    question = r.json()
except json.decoder.JSONDecode:
    print("Niepoprawny format")
else:
    pprint.pprint(question )
