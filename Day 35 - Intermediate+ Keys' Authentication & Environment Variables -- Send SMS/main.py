import requests

# my code was hardcoded, changed to using variables and dictionary after viewing solution video, which is a better way to do things
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "4eebf5128022ab276318eeb886a18211"
weather_params = {
    "lat": 43.653225,
    "lon": -79.383186,
    "appid": api_key,
    "units": "metric",
    "cnt": 4,
}

toronto_3_hr_weather = requests.get(OWM_Endpoint, params=weather_params)
toronto_3_hr_weather.raise_for_status()
# print(toronto_3_hr_weather.status_code)

# # my code for Challenge - Check if it Will Rain in the Next 12 Hours
# weather_data = toronto_3_hr_weather.json()["list"]
# for precip in weather_data:
#     if precip["weather"][0]["id"] < 700:
#         print("Bring an Umbrella")
#         break
#     else:
#         print("Don't bring an Umbrella")

# solution code for Challenge - Check if it Will Rain in the Next 12 Hours
will_rain = False
weather_data = toronto_3_hr_weather.json()
# print(weather_data["list"][0]["weather"][0]["id"])
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    print("Bring an Umbrella")