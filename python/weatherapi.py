import json , requests
r = requests.get('https://api.openweathermap.org/data/2.5/weather?q=cincinnati,us&&appid=f5d8298f3e7a0987b375d346886ab5c1')
data= r.json()
print(data)
print(data['weather'])
print(data['weather'][0]['description'])
