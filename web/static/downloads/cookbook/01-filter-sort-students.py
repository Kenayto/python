students = [
    {"name": "Anna", "points": 92},
    {"name": "Peter", "points": 67},
    {"name": "Lucia", "points": 84},
    {"name": "Marek", "points": 78},
]

qualified = [
    student for student in students
    if student["points"] >= 80
]

ranking = sorted(
    qualified,
    key=lambda student: student["points"],
    reverse=True,
)

for position, student in enumerate(ranking, start=1):
    print(f"{position}. {student['name']}: {student['points']} points")
