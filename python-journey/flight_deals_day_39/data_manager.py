import gspread
from oauth2client.service_account import ServiceAccountCredentials
from flight_search import FlightSearch

class DataManager:
    def __init__(self):
        self.cities = []
        self.flight_search = FlightSearch()
        self.iata_dict = {}
        self.sheet = None
    
    def sheet_data(self):
        # Define scope
        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive",
        ]
        # Load credentials
        # get your google_sheet_api.json file 
        creds = ServiceAccountCredentials.from_json_keyfile_name("google_sheet_api.json", scope)

        # Authorize
        client = gspread.authorize(creds)

        # Access the sheet
        sheet = client.open("Flight Deals").sheet1
        self.sheet = sheet

        # Get all values in the first row (header)
        headers = sheet.row_values(1)
        if "City" in headers:
            city_col_index = headers.index("City") + 1  # gspread is 1-indexed
            city_names = sheet.col_values(city_col_index)[1:]  # skip header
            self.cities = city_names  # store as flat list
            return self.cities
        else:
            print("DEBUG: 'City' column not found in sheet headers:", headers)
            return []

    def get_city_iata(self, city):
        return self.flight_search.get_iata_code(city)

    def get_cities_iata_dict(self, cities):
        """Return a dictionary mapping city names to their IATA codes."""
        for city in cities:
            iata_code = self.get_city_iata(city)
            if len(iata_code) == 3:
                self.iata_dict[city] = iata_code
                # return self.iata_dict
            else:
                read_colum = self.sheet.col_values(1)
                if city in read_colum:
                    index = read_colum.index(city) + 1
                    self.sheet.delete_rows(index)
        return self.iata_dict

    def put_iata_sheet(self):
        iata = [[value] for key, value in self.iata_dict.items()]
        self.sheet.update(F"B1" , [["IATA"]])
        return self.sheet.update(f"B2:B{len(self.iata_dict) + 1}", iata)

    