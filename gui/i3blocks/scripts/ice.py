#!/usr/bin/python

import requests

url = "https://iceportal.de/api1/rs/status"

try:
  r = requests.get(url)
  speed = int(r.json()['speed'])
  print(f" {speed} KM/H ")

except Exception:
  exit
