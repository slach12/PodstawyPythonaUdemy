import requests


response =requests.get("http://videokurs.pl")

print(response.status_code)
print(response.cookies)
print(response.text)

response =requests.get("http://2wp2.pl")

print(response.status_code)
print(response.cookies)
print(response.text)
