##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import pandas
import datetime as dt
import random
import smtplib

now = dt.datetime.now()
today_month = now.month
today_day = now.day

MY_EMAIL = "prettypisces56@gmail.com"
My_PASSWORD = "pythonTest23"

today_tuple = (today_month, today_day)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
print(birthday_dict)

