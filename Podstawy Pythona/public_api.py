import requests
import json



r = requests.get("")

try:
    question = r.json()
except json.decoder.JSONDecode:
    print("Niepoprawny format")
