# Lesson-1 example 5
# working with parameters and logical and arifmetic funstions

cashflow = 0
cost = 0
rent = 0
cash_tmp = input("""Для расчета показателей работы вашей фирмы
введите общую сумму выручки за последний месяц: """)


if cash_tmp.isdigit:
    cashflow = int(cash_tmp)
else:
    cashflow = int(input("Пожалуйста, используйте только цифры: "))


cost_tmp = input("Теперь укажите общую сумму расходов за последний месяц: ")

if cost_tmp.isdigit:
    cost = int(cost_tmp)
else:
    cost = int(input("Вводите только цифры пожалуйста: "))

if cashflow > cost:
    rent = (cashflow - cost) / cost * 100
    print(
        f"Ваша фирма работает в прибыль. Показатель рентабельности вашего бизнеса - {rent:.2f}%.")
else:
    print("Ваша фирма работает в убыток. Необходимо принимать меры по оптимизации расходов!")

count_people = input(
    "Для расчета показателя прибыли на одного сотрудника введите количество человек работающих в вашей фирме: ")

if count_people.isdigit:
    rent_by_pers = (cashflow - cost) / int(count_people)
    print(
        f"Показатель рентабельности на одного сотрудника вашей фирмы составляет: {rent_by_pers:.2f}")
else:
    print("Необходимо вводить количество человек в виде цифры")
