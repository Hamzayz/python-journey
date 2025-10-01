# type: ignore
import requests
from datetime import datetime

TOKEN = your_token
USERNAME = your_username
GRAPH_ID = graph_id

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token" :"aljklajglkajglkahlg" , 
    "username" : "hamzakhan" ,
    "agreeTermsOfService" :"yes" ,
    "notMinor" : "yes"
}

# data_url = requests.post(url="pixela_endpoint" , json=user_params)
# print(data_url.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id" : GRAPH_ID,
    "name" : "My walking graph" ,
    "unit" : "km" ,
    "type" : "float" ,
    "color" : "shibafu"
}
headers = {
    "X-USER-TOKEN" : TOKEN
}

# graph_url = requests.post(graph_endpoint , json=graph_config , headers=headers)

today = datetime(2025,7,3)
update_params = {
    "date" : today.strftime("%Y%m%d") , # https://www.w3schools.com/python/python_datetime.asp
    "quantity" : "5.5"
}

# update_graph = f"/v1/users/{USERNAME}/graphs/{GRAPH_ID}" 
update_graph = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
# new_data = requests.post(url=update_graph , json=update_params , headers=headers)
# print(new_data.text)

change_data = f"{update_graph}/20250702"
change_params = {
    "quantity": "12"
}
# update_data = requests.put(url=change_data , json=change_params , headers=headers)
# print(update_data.text)

delete_data = requests.delete(update_graph , headers=headers)
print(delete_data)
