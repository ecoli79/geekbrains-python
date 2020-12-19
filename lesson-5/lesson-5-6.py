# lesson-5 example 6
# working with files

# чтение даных из файла

# функция для получения часов из строки расписания по предмету

def getnumber(input_data):
    row_data = input_data.split()
    numbers = []
    if len(row_data):
        for i in range(1, len(row_data)):
            str_digits = ""
            for s in row_data[i]:
                if '0' <= s <= '9':
                    str_digits += s

            if str_digits != "":
                numbers.append(int(str_digits))
    return numbers


timetable = {}

print("По вашему курсу запланировано обучение по следующим предметам:")
print("-" * 45)
print("Предмет: общее количество часов")
print("-" * 45)

try:
    with open("example-6.txt", "r", encoding="utf-8") as file_input:
        for line in file_input.readlines():
            timetable[line.split()[0].replace(":", "")] = sum(getnumber(line))

    print(timetable)

except Exception as err:
    print(err)
