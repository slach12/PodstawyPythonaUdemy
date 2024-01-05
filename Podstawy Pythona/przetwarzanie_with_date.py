import requests
import json
import pprint
import webbrowser
from datetime import datetime, timedelta


print(datetime.today())
print(timedelta(days=7))

timeBefore = timedelta(days =10)
searchDate = datetime.today() - timeBefore


params = {
           "site" : "stackoverflow",
           "sort" : "votes",
           "order" : "desc",
           "fromdate" : int(searchDate.timestamp()),
           "tagged" : "python",
           "min" : 5
        }


r = requests.get("https://api.stackexchange.com/2.2/questions/", params)






try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
   # pprint.pprint(questions)
    for question in questions["items"]:
        webbrowser.open_new_tab(question["link"])
        pprint.pprint(question["link"])
       
