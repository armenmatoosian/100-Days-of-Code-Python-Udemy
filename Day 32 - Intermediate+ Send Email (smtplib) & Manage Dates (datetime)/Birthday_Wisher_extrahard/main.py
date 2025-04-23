##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas as pd
import random
import os
import smtplib

MY_EMAIL = "armen.100doc.udemy@gmail.com"
PASSWORD = "cyzscsngggnplzyq"

# 1. Update the birthdays.csv
# birthdays.csv has been modified

# 2. Check if today matches a birthday in the birthdays.csv - my code
today = dt.datetime.now()
today_month = today.month
today_day = today.day

# birthdays = pd.read_csv("birthdays.csv").to_dict(orient='records')
birthdays = pd.read_csv("birthdays.csv")
print(birthdays) # this is a check
print(birthdays["month"])
print(birthdays["day"])

# my code modified after watching solution video and using google Gemini to fix for more than one person having a birthday on the same day
birthday_person = {(data_row["name"], data_row["email"]) for (index, data_row) in birthdays.iterrows() if data_row["month"] == today_month and data_row["day"] == today_day}
print(birthday_person) # this is a check

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if birthday_person:
    for (name,email) in birthday_person:
        birthday_name = name
        birthday_email = email
        print(birthday_name) # this is a check
        print(birthday_email) # this is a check
        letter_templates = os.listdir("letter_templates")
        random_letter = random.choice(letter_templates)
        # print(random_letter) # this is a check
        with open(f"letter_templates/{random_letter}", "r") as letter:
            open_letter = letter.read()
        custom_letter = open_letter.replace("[NAME]", birthday_name)
        print(custom_letter) # this is a check

# 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthday_email,
                msg=f"Subject: Happy Birthday {birthday_name}!\n\n{custom_letter}"
                )

# # my original code before watching solution video
# birthday_person = [{"birthday_name": person["name"], "birthday_email": person["email"]} for person in birthdays if person["month"] == today_month and person["day"] == today_day]
# print(birthday_person) # this is a check
#
# # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# if birthday_person:
#     letter_templates = os.listdir("letter_templates")
#     random_letter = random.choice(letter_templates)
#     # print(random_letter) # this is a check
#     with open(f"letter_templates/{random_letter}", "r") as letter:
#         open_letter = letter.read()
#     custom_letter = open_letter.replace("[NAME]", birthday_person[0]["birthday_name"])
#     # print(custom_letter) # this is a check
#     birthday_email = birthday_person[0]["birthday_email"]
#     # print(birthday_email) # this is a check
#
# # 4. Send the letter generated in step 3 to that person's email address.
#     with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#         connection.starttls()
#         connection.login(user=MY_EMAIL, password=PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs=birthday_email,
#             msg=f"Subject: Happy Birthday {birthday_person[0]["birthday_name"]}!\n\n{custom_letter}"
#             )