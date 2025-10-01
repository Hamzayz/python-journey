# type: ignore
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
from datetime import datetime
import os

GENDER = "male"
WEIGHT_KG = "60"
HEIGHT_CM = "170"
AGE = "16"

APP_ID = your_app_id
API_KEY = your_api_key

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
scopes = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]
# get your own google_sheet_api.json file and import it
creds = ServiceAccountCredentials.from_json_keyfile_name("google_sheet_api.json" , scopes=scopes) #type: ignore
client = gspread.authorize(creds) #type: ignore
sheet = client.open("work").sheet1

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

bearer_headers = {
    "Authorization": "Bearer hamza2009"
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    rows = sheet_inputs["workout"]
    row = [value for (key , value) in rows.items()]
    sheet.append_row(row)


    