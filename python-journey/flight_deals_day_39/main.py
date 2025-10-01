import requests
from data_manager import DataManager
from flight_search import FlightSearch

flight_search  = FlightSearch()
datamanager = DataManager()

print(datamanager.get_cities_iata_dict(datamanager.sheet_data()))
print(datamanager.put_iata_sheet())

    

    
    # print(f"{city}: {datamanager.get_iata_code(city)}")