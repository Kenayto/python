import json
from pathlib import Path

data_file = Path(__file__).with_name("settings-sample.json")

try:
    with data_file.open("r", encoding="utf-8") as file:
        settings = json.load(file)
except FileNotFoundError:
    print(f"File not found: {data_file.name}")
except json.JSONDecodeError as error:
    print(f"Invalid JSON: {error}")
else:
    if not isinstance(settings, dict):
        print("Invalid settings: expected a JSON object.")
    else:
        print("Application:", settings.get("application", "Unknown"))
        print("Language:", settings.get("language", "en"))
        print("Notifications:", settings.get("notifications", False))
