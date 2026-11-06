import re

pattern = r"[A-Z]{2}\d{4}"
identifiers = ["AB1234", "xy1234", "ABC1234", "CD5678"]

for identifier in identifiers:
    if re.fullmatch(pattern, identifier):
        print(f"{identifier}: valid")
    else:
        print(f"{identifier}: invalid")
