from datetime import date

deadline_text = "2026-12-15"

try:
    deadline = date.fromisoformat(deadline_text)
except ValueError:
    print("Use the YYYY-MM-DD date format.")
else:
    today = date.today()
    difference = (deadline - today).days

    if difference > 0:
        print(f"{difference} days remaining.")
    elif difference == 0:
        print("The deadline is today.")
    else:
        print(f"The deadline passed {-difference} days ago.")
