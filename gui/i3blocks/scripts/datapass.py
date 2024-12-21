#!/usr/bin/python

import requests, humanize #, json

try:
  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0'}
  data = requests.get("https://datapass.de/api/service/generic/v1/status", headers=headers).json()
  
  # Unlimited
  if data.get("passType") == 102:
    print(f" unlimited {humanize.naturaldelta(data.get("remainingSeconds"))} ")
    exit
  
  remaining = (data.get("initialVolume") - data.get("usedVolume")) / 1024**3

  print(" {0:.2f} / {1:.0f} GB ".format(remaining, (data.get("initialVolume") / 1024**3)))
except Exception:
  exit
