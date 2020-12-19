# lesson-5 example 4
# working with files and lists

numbers = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре", "Five": "Пять",
           "Six": "Шесть", "Seven": "Семь", "Eight": "Восемь", "Nine": "Девять", "Ten": "Десять"}
out_line = []

try:
    with open("example-4.txt", "r", encoding="utf-8") as file_txt:
        for line in file_txt:
            if len(line):
                new_line = line.split()
                new_line.insert(0, numbers[new_line.pop(0)])
                out_line.append(new_line)

    # сохраняем полученный списко в файл out-example-4.txt
    with open("out-example-4.txt", "w", encoding="utf-8") as out_file:
        for line in out_line:
            out_file.writelines(" ".join(line) + "\n")

except Exception as err:
    print(err)
