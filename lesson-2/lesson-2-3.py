# Lesson-2 example 3
# working with dict and list - search element in collection by Python

dict_monthes_and_seasons = {1: "Зима", 2: "Зима", 3: "Весна", 4: "Весна", 5: "Весна",
                            6: "Лето", 7: "Лето", 8: "Лето", 9: "Осень", 10: "Осень", 11: "Осень", 12: "Зима"}

mountes = ["", "Январь", "Февраль", "Март", "Апрель", "Май",
           "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]


month = 0

number_of_month = input("Введите номер месяца в году: ")

while True:

    if number_of_month > "0" and number_of_month.isdigit:

        month = int(number_of_month)

        if 1 <= month < 13:

            print(
                f"{month} месяц относится к времени года {dict_monthes_and_seasons.get(month)} и имеет название {mountes[month]}")

            break

        else:

            number_of_month = input(
                "Такого месяца не существует! введите число от 1 до 12: ")
