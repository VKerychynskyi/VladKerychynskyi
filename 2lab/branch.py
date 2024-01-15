# Розгалуження if-else для визначення парності числа
number = 7
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

# Розгалуження elif для визначення оцінки студента
grade = 85
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")

# Вкладені розгалуження для визначення діапазону числа
value = 42
if value > 0:
    if value < 50:
        print(f"{value} is between 0 and 50.")
    else:
        print(f"{value} is greater than or equal to 50.")
else:
    print(f"{value} is less than or equal to 0.")