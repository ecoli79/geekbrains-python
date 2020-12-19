# lesson-5 example 7
# working with files and serialization
import json


firms = []

try:
    with open("example-7.txt", "r", encoding="utf-8") as file_input:
        data_input = file_input.readlines()

    sum_cashes = []
    sum_costs = []
    avarage_profits = []
    for line in data_input:
        firms.append({line.split()[0]: int(
            line.split()[2]) - int(line.split()[3])})

        sum_cashes.append(int(line.split()[2]))
        sum_costs.append(int(line.split()[3]))
        avarage_profits.append(int(line.split()[2]) - int(line.split()[3]))

    firms.append(
        {"Средняя_доходность": round(sum(avarage_profits) / len(avarage_profits))})
    print(firms)

    with open("firms.json", "w", encoding="utf-8") as output_data:
        json.dump(firms, output_data)


# проверка на правильность сохранения файла в json файле
    with open("firms.json", "r", encoding="utf-8") as input_data:
        data = json.load(input_data)
        print("Чтение данных из json файла:")
        print(data)

except Exception as err:
    print(err)
