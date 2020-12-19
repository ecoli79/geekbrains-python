# lesson-5 example 5
# working with files

import random

numbers = []

# генерируем числа и записываем их в файл example-5.txt
try:
    out_data = ""
    for i in range(1, 15):
        out_data += str(random.randint(13, 155)) + " "

    out_file = open("example-5.txt", "w", encoding="utf-8")
    out_file.write(out_data)
    out_file.close()

# читаем данные из файла example-5.txt
    with open("example-5.txt", "r", encoding="utf-8") as input_file:
        for line in input_file:
            if len(line):
                for dig in line.split():
                    numbers.append(int(dig))

    print(f"Сумма чисел в файле {out_file.name} составляет {sum(numbers)}")

except Exception as err:
    print(err)
