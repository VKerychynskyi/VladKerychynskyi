# Приклад 1: Проста функція Lambda для додавання двох чисел
addition = lambda x, y: x + y
result = addition(3, 5)
print("Result of addition:", result)

# Приклад 2: Використання функції Lambda в методі сортування списку
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
sorted_fruits = sorted(fruits, key=lambda fruit: len(fruit))
print("Sorted fruits by length:", sorted_fruits)

# Приклад 3: Використання функції Lambda у функції вибору
def operate_on_numbers(x, y, operation):
    return operation(x, y)

# Використання функції Lambda для визначення операції множення
multiplication_result = operate_on_numbers(4, 5, lambda a, b: a * b)
print("Multiplication result:", multiplication_result)