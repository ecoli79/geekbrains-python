# lesson-5 example 3
# working with files and list

# Чтение данных из файла и высысления с данными полученными из него

try:
    with open("example-3.txt", "r", encoding="utf-8") as file_txt:
        data_file = file_txt.readlines()

        # получаем список тех, у кого оклад ниже 20 тыс.
        print("Список сотрудников с зарплатой ниже 20 тыс. рублей:")
        print("-"*25)
        for el in data_file:
            if int(el.split()[1]) < 20:
                print(
                    f"Фамилия: {el.split()[0]}, заработная плата: {el.split()[1]} тысяч рублей")
        print("=" * 25)

        # подсчет средней з\п сотрудников
        sum_sallary = [int(el.split()[1]) for el in data_file]
        medium_salary = sum(sum_sallary) / len(sum_sallary)
        print(
            f"Средняя заработная плата составляет: {medium_salary} тысячи рублей")

except Exception as error:
    print(error)
