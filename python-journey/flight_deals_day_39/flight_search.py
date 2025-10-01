import os
import requests
from dotenv import load_dotenv
load_dotenv("flight-deals-start/keys.env")
FLIGHT_URL = "https://test.api.amadeus.com/v2/shopping/flight-offers"

class FlightSearch:
    def __init__(self):
        self._api_key = os.environ["API_KEY"]
        self._api_secret = os.environ["API_SECRET"]
        self._api_token = self.get_new_token()

    def get_new_token(self):
        self.token_header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        self.token_params = {
            "grant_type":"client_credentials" ,
            "client_id": self._api_key ,
            "client_secret": self._api_secret
        }
        token_request = requests.post("https://test.api.amadeus.com/v1/security/oauth2/token" , 
                                      headers=self.token_header ,
                                      data=self.token_params)
        token_request.raise_for_status()
        return token_request.json()["access_token"]
    
    def get_iata_code(self, city):
        url = "https://test.api.amadeus.com/v1/reference-data/locations"
        params = {
            "keyword": city,
            "subType": "CITY"
        }
        headers = {
            "Authorization": f"Bearer {self._api_token}"
        }
        
        try:
            response = requests.get(url, headers=headers, params=params)
            
            # If 401, get a new token and retry
            if response.status_code == 401:
                print(f"Token expired for {city}, getting new token...")
                headers = {"Authorization": f"Bearer {self._api_token}"}
                response = requests.get(url, headers=headers, params=params)
            
            data = response.json()
            
            # Check if data contains the expected structure
            if "data" in data and len(data["data"]) > 0:
                iata = data['data'][0]['iataCode']
                return iata
            else:
                # Try with partial city name (first word)
                partial = city.split()[0]
                params['keyword'] = partial
                response = requests.get(url, headers=headers, params=params)
                data = response.json()
                if 'data' in data and len(data['data']) > 0:
                    iata = data['data'][0]['iataCode']
                    return iata
                else:
                    return f"{city}"
  
        except Exception as e:
            print(f"Error getting IATA code for {city}: {e}")
            return None
    



