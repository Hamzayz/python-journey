import requests
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# Enviromental variables:
# the virabiles which are fixed and stored in your system
# they are used to secure your API_keys form not pubiclic them and make a 
# different box where you API_keys are safe and move away from your code
# you can see that keys by writing evn in terminal and for adding a key you will write evn:NAME_OF_KEY=key
# to get that key you will be using os module like os.environ.get(NAME_OF_KEY)

GMAIL = "mhamzayz.ai@gmail.com"
PASSWORD = "jobx sest lkgt otsz"
API_KEY = "962579395e0e4e2b9b2af06aa652885c"
parameters = {
    "lon" :  71.533057,
    "lat" : 34.006962 ,
    "appid" : API_KEY,
    "cnt" : 4
}

data_url = requests.get("https://api.openweathermap.org/data/2.5/forecast?" , params=parameters)

data_url.raise_for_status()
data = data_url.json()


# for number in range(0,4):
#     weater = (data["list"][number]["weather"][0]["id"])
#     if weater < 700 :
#         print("Its raining out there")

will_rain = False
for hour_data in data["list"]:
    condition_code = (hour_data["weather"][0]["id"])
    if condition_code < 700:
        will_rain = True
        
if will_rain:
    subject = "RAIN ALERT 🌧️"
    body = "Today it will be raining out there so take your emblara with you."
    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = Header(subject, "utf-8")
    msg["From"] = GMAIL
    msg["To"] = "hamzaisrar1251@gmail.com"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=GMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=GMAIL,
            to_addrs="hamzaisrar1251@gmail.com",
            msg=msg.as_string()
        )
# print(os.environ.get("OPENWEATHER_API_KEY"))


