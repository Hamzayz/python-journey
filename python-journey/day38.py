# import gspread
# from google.oauth2.service_account import Credentials

import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define scope
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]

# Load credentials
# get your google_sheet_api.json file and import it
creds = ServiceAccountCredentials.from_json_keyfile_name("google_sheet_api.json", scope)

# Authorize
client = gspread.authorize(creds)

# Access the sheet
sheet = client.open("work").sheet1

# # Add headers
# sheet.update('A1', [['Name', 'Subject', 'Marks']])

# # # Add a row
# sheet.append_row(['Hamza', 'Science', 88])

# Delete the 2nd row (Hamza's data)

sheet.delete_rows(3)

# # Delete 3rd column (Marks)
# sheet.delete_columns(2)


# Example: read all data
print(sheet.get_all_records())














# scopes = [
#     "https://www.googleapis.com/auth/spreadsheets"
# ]
# creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
# client = gspread.authorize(creds)
# sheets_id = "1DHL6Y8XAHSC_KhJsa9QMekwP8b4YheWZY_sxlH3i494"
# spreadsheet = client.open_by_key(sheets_id)

# # Get all worksheet objects
# worksheets = spreadsheet.worksheets()

# # Print the title of each worksheet
# for ws in worksheets:
#     print(ws.title)