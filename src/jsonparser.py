import json

def parse_json(date):
    with open("resources/weather.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    daily = data.get("daily", [])

    result = [entry for entry in daily if entry.get("date") == date]

    return result

target_date = "2024-08-19"
print(parse_json(target_date))
