import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

url = "https://richdemo.euw1v1.netboxapp.com:443/api/wireless/wireless-lans/"

payload = json.dumps([
  {
    "ssid": "B_WIFI",
    "description": "Branch Office Wifi",
    "group" : 9, 
    "vlan": 48, 
    "tenant": 3,
    "auth_type": "wpa-enterprise",
    "auth_psk": "5up3r5ecr3tK3y",
    "auth_cipher": "aes"
  },
  {
    "ssid": "G_WIFI",
    "description": "Guest Wifi",
    "group" : 9, 
    "vlan": 49, 
    "tenant": 3,
    "auth_type": "wpa-enterprise",
    "auth_psk": "M3g45ecr3tK3y",
    "auth_cipher": "aes"
  }
  ])
headers = {
  'Content-Type': 'application/json',
  'Authorization': os.getenv('api_token')
}

r = requests.request("POST", url, headers=headers, data=payload)
pretty_json = json.loads(r.text)
print (json.dumps(pretty_json, indent=4))