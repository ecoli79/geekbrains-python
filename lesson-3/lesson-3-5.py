# lesson 3 example 5
# working with function


def summary_digits(input_string):
    """Суммирование чисел полученных в параметрах функции"""

    digits = [int(item) for item in input_string.split()]
    return sum(digits)


summ = 0

while True:

    input_data = input(
        "Введите несколько чисел через запятую для выхода из программы наберите Q: ").upper()

    if "Q" not in input_data:
        summ += summary_digits(input_data)

        print(f"Сумма введенных чисел равна: {summ}")

    else:
        summ += summary_digits(input_data.replace("Q", ""))
        print(f"Сумма введенных чисел равна: {summ}")
        break
