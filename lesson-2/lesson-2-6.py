# Lesson-2 example 6
# working with list and tuple and other type data by Python

item_name = ''
item_price = float
item_count = int
item_ei = ''
goods = []
itog = dict.fromkeys(['название', 'цена', 'количество', 'ед'])
i = 1
list_of_names = []
list_of_prices = []
list_of_counts = []
list_of_eds = []

while True:

    while i < 5:

        item_name = input(
            f"Формирование каталога для интернет магазина. Введите наименование товара под номером {i}: ")

        input_string = input("Введите стоимость данного товара: ")

        if input_string.isdecimal:

            item_price = float(input_string)

        else:

            item_price = input(
                "Вы ввели не цифры! Введите стоимость товара цифрами: ")

            item_price = float(input_string)

        input_string = input("Введите количество товара цифрами: ")

        if input_string.isdigit:

            item_count = int(input_string)

        else:

            item_count = input(
                "Вы ввели не цифры! Введите количество товара цифрами: ")

            item_count = int(input_string)

        item_ei = input("Введите единицы измерения товара, например шт.: ")

        goods.append((i, {"наименование": item_name, "цена": item_price,
                          "количество": item_count, "ед": item_ei}))

        i += 1

    for good in goods:

        list_of_names.append(good[1]['наименование'])
        list_of_prices.append(good[1]['цена'])
        list_of_counts.append(good[1]['количество'])
        list_of_eds.append(good[1]['ед'])

    itog['название'] = list(set(list_of_names))
    itog['цена'] = list(set(list_of_prices))
    itog['количество'] = list(set(list_of_counts))
    itog['ед'] = list(set(list_of_eds))

    print("=============================================================")
    print(f"В нашем интернет магазине сейчас {len(goods)} позиций товара")
    print(
        f"Масимальная цена товара по нашему каталогу составляет {max(list_of_prices)} рублей")
    print(
        f"Всего количество единиц товара в настоящий момент {sum(list_of_counts)} штук")
    print(itog)

    break
