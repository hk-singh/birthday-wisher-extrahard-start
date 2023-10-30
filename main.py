##################### Birthday wisher app ######################
import smtplib
import datetime as dt
import random
import pandas as pd

# declare emailid and password
my_email = ""
password = ""

# 1. Update the birthdays.csv
df = pd.read_csv("birthdays.csv")
birthdays_list = df.values.tolist()
# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
# function to find out whom to wish on a specific day of the month and return their name and email id
def who_to_wish():
    for i in range(0, len(birthdays_list)):
        if birthdays_list[i][3] == now.month and birthdays_list[i][4] == now.day:
            name = birthdays_list[i][0]
            email_id = birthdays_list[i][1]
            return name, email_id


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's
# actual name from birthdays.csv
name, email_id = who_to_wish()
letter_number = random.randint(1, 3)
# Open a random letter
with open(f"letter_templates/letter_{letter_number}.txt") as letter:
    letter_text = letter.read().replace("[NAME]", name)
    print(letter_text)


# 4. Send the letter generated in step 3 to that person's email address.
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs=email_id,
#         msg=f"Subject:Birthday wishes\n\n {letter_text}")








