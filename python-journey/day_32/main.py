##################### Hard Starting Project ######################
import datetime as dt
import pandas
import random
import smtplib

# 1. Get today's month and day
today = dt.datetime.now()
today_tuple = (today.month, today.day)

# 2. Read the birthdays CSV file
birthdays_df = pandas.read_csv("day32/birthdays.csv")

# 3. Create a dictionary with (month, day) as keys
birthdays_dict = {(row.month, row.day): row for index, row in birthdays_df.iterrows()}

# 4. Read letter templates
with open("day32/letter_templates/letter_1.txt") as letter_file:
    letter_1 = letter_file.read()
with open("day32/letter_templates/letter_2.txt") as letter_file:
    letter_2 = letter_file.read()
with open("day32/letter_templates/letter_3.txt") as letter_file:
    letter_3 = letter_file.read()

letters = [letter_1, letter_2, letter_3]

# 5. Check if today matches a birthday
if today_tuple in birthdays_dict:
    person = birthdays_dict[today_tuple]
    name = person.name
    email = person.email

    # 6. Pick a random letter and personalize it
    chosen_letter = random.choice(letters)
    personalized_letter = chosen_letter.replace("[NAME]", name)

    # 7. Send the email
    gmail = "your_gmail"
    password = "your_app_password_here"  # <-- Use your real app password

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=gmail, password=password)
        connection.sendmail(
            from_addr=gmail,
            to_addrs=email,
            msg=f"Subject:Happy Birthday!\n\n{personalized_letter}"
        )

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



