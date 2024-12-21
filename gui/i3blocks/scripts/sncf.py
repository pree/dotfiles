#!/usr/bin/python

import requests

url = "https://wifi.sncf/router/api/train/gps"

try:
  r = requests.get(url)
  speed = int(r.json()['speed']*3.6)
  print(f" {speed} KM/H ")

except Exception:
  exit
