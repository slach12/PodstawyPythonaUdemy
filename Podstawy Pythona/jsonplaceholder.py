import requests
import json

r = requests.get("https://jsonplaceholder.typicode.com/todos")

#print(r.text)

#tasks = json.loads(r.text)
try:
    tasks = r.json()
except json.JSONDecodeError:
    print("Niepoprawny format")
else:
    print("Wszystko jest ok.")
    print(tasks[0])
