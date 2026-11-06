from collections import Counter

topics = [
    "Python", "Databases", "Python",
    "OOP", "Python", "Databases",
    "Files", "OOP", "Python",
]

counts = Counter(topics)

for topic, amount in counts.most_common():
    print(f"{topic}: {amount}")
