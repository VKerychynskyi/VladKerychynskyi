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