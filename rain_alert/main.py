import requests
import os

MY_LAT = 41.997345
MY_LONG = 21.427996
API_KEY = os.getenv('OWM_API_KEY')

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "cnt": 4
}

will_rain = False
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()
for item in data["list"]:
    if int(item["weather"][0]['id']) < 700:
        will_rain = True
if will_rain:
    print("Bring an umbrella")
