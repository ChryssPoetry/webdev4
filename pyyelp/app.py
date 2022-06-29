#app
from email import header
import requests
import config
url = "https://api.yelp.com/v3/businesses/search"


headers = {
    "Authorization": "Bearer " + config.api_key

}
params = {
    "terms": "barber",
    "location" : "NYC"
}
response = requests.get(url, headers=headers, params=params)
""" converting the result to a dictionary"""

businesses = response.json()["businesses"]
names = [business["name"] 
    for business in businesses 
    if business["rating"] > 4.5 ]
print(names)
#hiding API keys


