#!/usr/bin/python

import requests

url = "https://iceportal.de/api1/rs/status"

states = {
  "HIGH": "Schnelles Internet",
  "MIDDLE": "Schnelles Internet",
  "WEAK": "Langsames Internet",
  "UNSTABLE": "Wechselhaftes Internet",
  "NO_INFO": "Internet verfügbar",
  "NO_INTERNET": "Kein Internet"
}

try:
  r = requests.get(url)
  state = states.get(r.json()['connectivity']['currentState'])
  print(f" {state} ")

except Exception:
  exit
