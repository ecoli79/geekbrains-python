# lesson-5 example 2
# working with files

# Чтение данных из текстового файла

try:
    data_file = []
    with open("example-2.txt", "r", encoding="utf-8") as file_txt:
        data_file = file_txt.readlines()
        print(f"В файле {file_txt.name}: {len(data_file)} строк:")

        for i, ln in enumerate(data_file):
            print(f"В строке {i+1} - {len(list(ln.split()))} слов")

except Exception as err:
    print(err)
