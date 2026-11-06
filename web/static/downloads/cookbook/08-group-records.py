from collections import defaultdict

students = [
    {"name": "Anna", "course": "Python"},
    {"name": "Peter", "course": "Databases"},
    {"name": "Lucia", "course": "Python"},
    {"name": "Marek", "course": "OOP"},
    {"name": "Eva", "course": "Databases"},
]

groups = defaultdict(list)

for student in students:
    groups[student["course"]].append(student["name"])

for course, names in sorted(groups.items()):
    print(f"{course}: {', '.join(names)}")
