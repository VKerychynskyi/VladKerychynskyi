# Цикл for для ітерації по списку
fruits = ["apple", "banana", "cherry"]
print("Fruits in the list:")
for fruit in fruits:
    print(fruit)

# Цикл while для виведення чисел від 1 до 5
counter = 1
print("\nCounting from 1 to 5:")
while counter <= 5:
    print(counter)
    counter += 1

# Цикл for з використанням range() для створення списку чисел
print("\nSquares of numbers from 1 to 5:")
for num in range(1, 6):
    square = num ** 2
    print(f"{num} squared is {square}")