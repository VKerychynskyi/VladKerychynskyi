# Звіт до роботи
## Тема: _Основи програмування на Python_
### Мета роботи: _Навчитися основам програмування python_

---
### Виконання роботи
* Результати виконання завдання ;
   
    1. Приклад програми з простими змінними, списками list, наборами set та словниками dict
   
 name = "John"
 age = 25
 height = 1.75
 grades = [95, 89, 78, 92, 87]
 hobbies = {"reading", "coding", "gaming", "traveling"}
 person_info = {
    "name": "John",
    "age": 25,
    "height": 1.75,
    "grades": [95, 89, 78, 92, 87],
    "hobbies": {"reading", "coding", "gaming", "traveling"}
 }
 print(f"Name: {name}")
 print(f"Age: {age}")
 print(f"Height: {height}m")
 print(f"Grades: {grades}")
 print(f"Hobbies: {hobbies}")
 print("\nPerson Information:")
 print(f"Name: {person_info['name']}")
 print(f"Age: {person_info['age']}")
 print(f"Height: {person_info['height']}m")
 print(f"Grades: {person_info['grades']}")
 print(f"Hobbies: {person_info['hobbies']}")

Програма вивела
![alt text](./picture/Screenshot56.png "Результат програми")
 
 1. Приклад програми виведення вбудованих констант
    import math


print(f"Pi (π): {math.pi}")


print(f"Euler's number (e): {math.e}")


print(f"Infinity: {float('inf')}")

Прогама вивела
![alt text](./picture/Screenshot57.png "Результат програми")
    
1. Створив програму виведення результату роботи вбудованих функцій 
    
my_list = [1, 2, 3, 4, 5]
length_of_list = len(my_list)
print(f"Length of the list: {length_of_list}")


numbers = [10, 20, 30, 40, 50]
sum_of_numbers = sum(numbers)
print(f"Sum of numbers: {sum_of_numbers}")

max_value = max(numbers)
print(f"Maximum value in the list: {max_value}")


pi_value = 3.14159
rounded_pi = round(pi_value, 2)
print(f"Rounded value of Pi: {rounded_pi}")
Програма вивела
![alt text](./picture/Screenshot58.png "Результат програми")


1.  Написав код який демонструє роботу циклів
   
fruits = ["apple", "banana", "cherry"]
print("Fruits in the list:")
for fruit in fruits:
    print(fruit)


counter = 1
print("\nCounting from 1 to 5:")
while counter <= 5:
    print(counter)
    counter += 1


print("\nSquares of numbers from 1 to 5:")
for num in range(1, 6):
    square = num ** 2
    print(f"{num} squared is {square}")
    Програма вивела

![alt text](./picture/Screenshot59.png "Результат програми")

1. Написав код який демонструє роботу розгалужень

number = 7
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")


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


value = 42
if value > 0:
    if value < 50:
        print(f"{value} is between 0 and 50.")
    else:
        print(f"{value} is greater than or equal to 50.")
else:
    print(f"{value} is less than or equal to 0.")

програма вивела
![alt text](./picture/Screenshot60.png "Результат програми")
   
   1.Конструкція try->except->finally. Написав свій варіант коду з помилкою.
try:
    # Введення числа від користувача
    user_input = input("Введіть число: ")

    # Спроба конвертувати введення у ціле число
    number = int(user_input)

    # Ділення на нуль для виклику помилки
    result = 10 / number

except ValueError:
    # Обробка помилки, яка виникає, коли користувач вводить нечислові дані
    print("Помилка: Введено нечислове значення.")

except ZeroDivisionError:
    # Обробка помилки, яка виникає при діленні на нуль
    print("Помилка: Ділення на нуль.")

finally:
    # Код, який виконується завжди, незалежно від того, чи сталася помилка чи ні
    print("Блок finally виконується завжди.")
    Програма вивела

![alt text](./picture/Screenshot61.png "Результат програми")
   
1.Написав свій код з контекст-менеджером
   class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()


with FileManager("example.txt", "r") as file:
    try:
        content = file.read()
        print(content)
    except Exception as e:
        print(f"Помилка: {e}")
        
        Програма вивела
   ![alt text](./picture/Screenshot62.png "Результат програми")
    
 1.  Написав свій приклад коду з lambdas
   
addition = lambda x, y: x + y
result = addition(3, 5)
print("Result of addition:", result)

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
sorted_fruits = sorted(fruits, key=lambda fruit: len(fruit))
print("Sorted fruits by length:", sorted_fruits)


def operate_on_numbers(x, y, operation):
    return operation(x, y)


multiplication_result = operate_on_numbers(4, 5, lambda a, b: a * b)
print("Multiplication result:", multiplication_result)
 Програма вивела
 ![alt text](./picture/Screenshot63.png "Результат програми")




  
---
### Висновок:
 Навчився створювати програми з простими змінними, списками list, наборами set та словниками dict
 Навчився створювати програми виведення вбудованих констант import math
 Навчився створювати програму виведення результату роботи вбудованих функцій 
 Навчився писати код який демонструє роботу циклів   
 Навчився писати код який демонструє роботу розгалужень
 Вивчив конструкцію try->except->finally
 Написав свій код з контекст-менеджером
  Написав свій приклад коду з lambdas