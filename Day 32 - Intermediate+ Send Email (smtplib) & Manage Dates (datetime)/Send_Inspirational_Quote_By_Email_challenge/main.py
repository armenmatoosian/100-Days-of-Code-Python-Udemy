# my code for Challenge 1 - Send Motivational Quotes on Mondays via Email
import datetime as dt
import random
import smtplib

# changed to constant after watching solution video
MY_EMAIL = "armen.100doc.udemy@gmail.com"
PASSWORD = "cyzscsngggnplzyq"

# solution code had the two following lines within the if statement below, though the below works, as well
with open(file="quotes.txt") as quotes_file:
    random_quote = random.choice(quotes_file.readlines())

now = dt.datetime.now()
if now.weekday() == 1:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user="armen.100doc.udemy@gmail.com", password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="armen_100doc_udemy@yahoo.com",
            msg=f"Subject:Monday Inspirational Quote\n\nHappy Monday!\n\n Here's this week's inspirational quote.\n\n{random_quote}"
        )

# this is a check
print(random_quote)

#----------------------------------------------------------------------------------------------------------------------#
# starting exercises for Day 32
# import smtplib
#
# my_email = "armen.100doc.udemy@gmail.com"
# password = "cyzscsngggnplzyq"
#
# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     # connection = smtplib.SMTP('smtp.gmail.com', 587) # can eliminate this using with
#     connection.starttls()
#     connection.login(user="armen.100doc.udemy@gmail.com", password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="armen_100doc_udemy@yahoo.com",
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )
# # connection.close() # can eliminate this using with

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day = now.day
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1991, month=10, day=28, hour=4)
# print(date_of_birth)