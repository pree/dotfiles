#!/usr/bin/python

import requests
import re
import json

url = "https://www.ombord.info/api/jsonp/position/"

try:
  r = requests.get(url)
  data = json.loads(re.match(".*?({.*}).*",r.text,re.S).group(1))
  speed = int(float(data['speed'])*3.6)
  print(f" {speed} KM/H ")

except Exception:
  exit
