import requests
import json
import os
from dotenv import load_dotenv

# Load the .env file so the API Token can be read by the script
load_dotenv()

# Set the 'token' variable to the value of 'api_token' from the .env file
# Rename file .env.example to .env and add your own API token
# Remember to add .env to your .gitignore file to avoid uploading the token to your Git repo
token = os.getenv('api_token') 

# Set variables to match your own NetBox installation
nb_protocol = 'http' 
nb_host = 'netbox'
nb_port = '8000'

# Build the URL for the API request
url = nb_protocol+'://'+nb_host+':'+nb_port+"/api/wireless/wireless-lans/"

# Set the payload and headers for the API request
payload = json.dumps([
  {
    "ssid": "B_WIFI",
    "description": "Branch Office Wifi",
    "group" : 1, 
    "vlan": 3, 
    "tenant": 5,
    "auth_type": "wpa-enterprise",
    "auth_psk": "5up3r5ecr3tK3y",
    "auth_cipher": "aes"
  },
  {
    "ssid": "G_WIFI",
    "description": "Guest Wifi",
    "group" : 1, 
    "vlan": 4, 
    "tenant": 5,
    "auth_type": "wpa-enterprise",
    "auth_psk": "M3g45ecr3tK3y",
    "auth_cipher": "aes"
  }
  ])
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Token '+ token
}

# Send the API request and display the result in pretty json format
response = requests.request("POST", url, headers=headers, data=payload)
pretty_json = json.loads(response.text)
print (json.dumps(pretty_json, indent=4))