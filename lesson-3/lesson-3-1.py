# lesson-3 example 1
# working with fanctions

def division_digits(dig1, dig2):
    """devision to digitals"""

    try:
        print(f"{dig1/dig2:.2f}")
    except ZeroDivisionError:
        print("Ошибка! Деление на ноль!")


division_digits(int(input("Введите делимое число: ")),
                int(input("Введите делитель: ")))
