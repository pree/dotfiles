#!/usr/bin/python

import requests
from datetime import datetime, timezone
import humanize

try:
    probe_id = ""
    r = requests.get("https://atlas.ripe.net/api/v2/probes/" + probe_id)
    status = r.json()["status"]
    since = datetime.fromisoformat(status['since'].replace("Z", "+00:00"))
    offset = datetime.now(timezone.utc) - since

    if status["id"] == 2:
        #offset = datetime.now(timezone.utc) - since
        icon = ""
        color = "#E00201"
    else:
        #offset = since - datetime.now(timezone.utc)
        icon = ""
        color = "#008000"

    print(f" <span foreground='{color}'>{icon}</span> {humanize.naturaldelta(offset)} ")
    print(f"{icon}")
except Exception:
    exit
