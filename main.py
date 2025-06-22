#  Emanuel Biruk Seifegebreal - 2024 --> Project for learning purposes
import datetime as dt
import pandas
import random
import smtplib
# The password and email don't work there are just placeholders. The program's logic does work though.
MY_EMAIL = "email"
PASSWORD = "blablabla"

now = dt.datetime.now()
today_tuple = (now.month, now.day)

data = pandas.read_csv("birthdays.csv")

data_dict = data.to_dict(orient="records")

birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="blablablan@yahoo.com",
                            msg=f"Subject:Happy Birthday!\n\n{contents}"
                            )
