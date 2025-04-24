# code for Working with Responses: HTTP Codes, Exceptions & JSON Data
import requests
from datetime import datetime
import smtplib
import time

# email info
MY_EMAIL = "armen.100doc.udemy@gmail.com"
PASSWORD = "cyzscsngggnplzyq"

# Toronto latitude and longitude
MY_LAT = 43.6532
MY_LONG = 79.3832

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_long = float(data["iss_position"]["longitude"])
iss_lat = float(data["iss_position"]["latitude"])

iss_position = (iss_lat, iss_long)

# print(iss_position)

# shared code for Understand API Parameters: Match Sunset Times with the Current Time
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

# print(sunrise)
# print(sunset)

time_now = datetime.now()

# print(time_now.hour)

# my code for ISS Overhead Notifier Project - Challenge & Solution
# If the ISS is close to my current position
def is_iss_close():
    # my original code - incorrect syntax
    # if MY_LAT is (iss_position[0]-5) <= iss_position[0] <= (iss_position[0]+5) and MY_LONG is (iss_position[1]-5) <= iss_position[1] <= (iss_position[1]+5):
    if MY_LAT-5 <= iss_position[0] <= MY_LAT+5 and MY_LONG-5 <= iss_position[1] <= MY_LONG+5:
        iss_is_close = True
        # print(iss_is_close)
    else:
        iss_is_close = False
        # print(iss_is_close)
    return iss_is_close

print(is_iss_close())

# and it is currently dark
def is_it_dark():
    # my original code - condition doesn't work properly around midnight
    # if sunset <= time_now.hour <= sunrise:
    if time_now.hour >= sunset or time_now.hour <= sunrise:
        it_is_dark = True
    else:
        it_is_dark = False
    return it_is_dark

print(is_it_dark())


# Then send me an email to tell me to look up.
# solution code for ISS Overhead Notifier Project - Challenge & Solution
# BONUS: run the code every 60 seconds. -- while loop portion
while True:
    time.sleep(60)
    if is_iss_close() and is_it_dark():
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="armen_100doc_udemy@yahoo.com",
                msg=f"Subject: Look Up!\n\nIt's dark, and the ISS is overhead."
            )
    elif not is_iss_close() and is_it_dark():
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="armen_100doc_udemy@yahoo.com",
                msg=f"Subject: DON'T Look Up!\n\nIt's dark, but the ISS is NOT overhead."
            )