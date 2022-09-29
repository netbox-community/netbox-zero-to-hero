import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

url = "https://richdemo.euw1v1.netboxapp.com:443/api/wireless/wireless-lan-groups/?brief=1"

payload = ""
headers = {
  'Content-Type': 'application/json',
  'Authorization': os.getenv('api_token')
}

r = requests.request("GET", url, headers=headers, data=payload)
pretty_json = json.loads(r.text)
print (json.dumps(pretty_json, indent=4))