import csv
from pathlib import Path

csv_file = Path(__file__).with_name("students-sample.csv")
scores = []

try:
    with csv_file.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            points = row.get("points")
            if points is None or not points.strip():
                raise ValueError("Missing points value")
            scores.append(int(points))
except FileNotFoundError:
    print(f"File not found: {csv_file.name}")
except (KeyError, ValueError) as error:
    print(f"Invalid CSV data: {error}")
else:
    if scores:
        average = sum(scores) / len(scores)
        print(f"Records: {len(scores)}")
        print(f"Average score: {average:.1f}")
    else:
        print("The CSV file contains no records.")
