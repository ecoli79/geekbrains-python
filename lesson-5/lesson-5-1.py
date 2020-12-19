# lesson-5 example 1
# working with files

# создание файла и запись в него данных

def write_file(write_data):
    with open("example-1.txt", "a") as file_txt:
        file_txt.write(write_data + "\n")


print("Для записи данных в файл введите их в нижнее поле.")
print("Для сохранения файла нажмите Enter при пустой строке.")

try:
    while True:

        data_file = input(
            "Введите данные для записи в файл example-1.txt в текущей директории: ")

        if len(data_file):
            write_file(data_file)
        else:
            write_file("")
            break

except Exception as err:
    print(err)
