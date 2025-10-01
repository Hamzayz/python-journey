
from datetime import datetime
import requests

# REQUESTS MODULE :
# request.get() to get some data from website or a server and expect some responce
# request.post() to put some data to a surver for a website and don't expect any responve
# request.put() to update the data in the website and server
# request.delete() to delete some data 

MY_LATITUDE = 34.006962
MY_LONGITUDE = 71.533057

pramaters= {
    "lat":MY_LATITUDE,
    "lng":MY_LONGITUDE,
    "formatted":0
}
data_url = requests.get(url="https://api.sunrise-sunset.org/json" , params=pramaters )
data_url.raise_for_status()
data = data_url.json()
sunrise = (data)["results"]["sunrise"]
sunset = (data)["results"]["sunset"]


print(sunrise.split("T")[1].split(":")[0])
print(sunset.split("T")[1].split(":")[0])

now = datetime.now().hour
print(now)