# Прості змінні
name = "John"
age = 25
height = 1.75

# Список (list)
grades = [95, 89, 78, 92, 87]

# Набір (set)
hobbies = {"reading", "coding", "gaming", "traveling"}

# Словник (dict)
person_info = {
    "name": "John",
    "age": 25,
    "height": 1.75,
    "grades": [95, 89, 78, 92, 87],
    "hobbies": {"reading", "coding", "gaming", "traveling"}
}

# Виведення інформації
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}m")
print(f"Grades: {grades}")
print(f"Hobbies: {hobbies}")

# Виведення інформації зі словника
print("\nPerson Information:")
print(f"Name: {person_info['name']}")
print(f"Age: {person_info['age']}")
print(f"Height: {person_info['height']}m")
print(f"Grades: {person_info['grades']}")
print(f"Hobbies: {person_info['hobbies']}")