# Lesson-2 example 5
# working with list by Python

my_list = [2, 3, 5, 7, 8]

new_rate = input("Введите любое число в пределах от 0 до 20: ")

while True:

    if new_rate.isdigit:

        rate_add = int(new_rate)

        if 0 <= rate_add <= 20:

            if rate_add in my_list:

                my_list.insert(my_list.index(rate_add) + 1, rate_add)

                my_list.reverse()

                print(my_list)

                break
            else:

                my_list.append(rate_add)

                my_list.sort(reverse=True)

                print(my_list)

            break

        else:

            new_rate = input(
                "Вы ввеле неверное число! Введите число в пределах от 0 до 20: ")
