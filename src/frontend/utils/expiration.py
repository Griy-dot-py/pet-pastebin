import json

never = json.dumps({})
ten_minutes = json.dumps({"minutes": 10})
hour = json.dumps({"hours": 1})
day = json.dumps({"days": 1})
week = json.dumps({"days": 7})
two_weeks = json.dumps({"days": 14})
month = json.dumps({"months": 1})
half_year = json.dumps({"month": 6})
year = json.dumps({"months": 11, "days": 30, "hours": 23, "minutes": 59})
