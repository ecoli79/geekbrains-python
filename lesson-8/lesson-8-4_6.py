# lesson-8 example 4-6
# workking with OOP project


class Warehouse:
    goods = []

    def income_equipment(self, object, count):
        if count >= 0:
            self.goods.append({"type": object.params[0], "name": object.params[1],
                               "param": object.params[3], "price": object.params[2], "count": count})
        else:
            print("Количество товара должно быть больше 0")

    def outcome_equipment(self, type_equip, param, count):
        if count > 0:
            for el in self.goods:
                if el["type"] == type_equip and el["param"] == param:
                    el["count"] -= count
                    print(
                        f"Выдано {type_equip} cо следующими характеристиками {param} в количестве {count}")
                    self.inventory()
        else:
            print("Количество должно быть больше 0")

    def inventory(self):
        print("Остатки на складе:")
        print("-" * 29)
        for el in self.goods:
            print(el)


class Equipments:
    name = ""
    price = ""

    def __init__(self):
        self.name = input(f"Введите наименование {self.__class__.__name__}: ")
        self.price = float(
            input(f"Введите стоимость {self.__class__.__name__}: "))


class Printer(Equipments):

    @classmethod
    def set_format(self):
        self.format = input("Введите формат принтера: ")

    @property
    def params(self):
        return (self.__class__.__name__, self.name, self.price, self.format)


class Scaner(Equipments):

    @classmethod
    def set_typescaner(self):
        self.typescaner = input("Введите тип сканера: ")

    @property
    def params(self):
        return (self.__class__.__name__, self.name, self.price, self.typescaner)


class Xerox(Equipments):
    @classmethod
    def set_size(self):
        self.size = input("Введите размер копира: ")

    @property
    def params(self):
        return (self.__class__.__name__, self.name, self.price, self.size)


warehouse1 = Warehouse()

while True:
    print("Выберите действие: ")
    print("Поступление        - 1")
    print("Выдача в отдел     - 2")
    print("Инвентаризация     - 3")
    print("Выход из программы - q")
    in_data = input()

    if in_data in ("1", "2", "3", "q", "Q"):
        if in_data == "1":
            while True:
                print("Выберите тип оборудования которое будет принятно на склад:")
                print("Принтер - 1")
                print("Сканер  - 2")
                print("Ксерокс - 3")
                print("Пустая строка чтобы закончить ввод.")
                in_data = input()
                if in_data in ("1", "2", "3", " "):
                    if in_data == "1":
                        try:
                            printer = Printer()
                            Printer.set_format()
                            count = int(input("Введите количество: "))
                            warehouse1.income_equipment(printer, count)
                        except Exception as err:
                            print(err)
                    if in_data == "2":
                        try:
                            scaner = Scaner()
                            Scaner.set_typescaner()
                            count = int(input(f"Введите количество: "))
                            warehouse1.income_equipment(scaner, count)
                        except Exception as err:
                            print(err)
                    if in_data == "3":
                        try:
                            xerox = Xerox()
                            Xerox.set_size()
                            count = int(input("Введите количество: "))
                            warehouse1.income_equipment(xerox, count)
                        except Exception as err:
                            print(err)
                    if in_data == " ":
                        break
    if in_data == "2":
        while True:
            print("Выберите тип оборудования которое будет выдано:")
            print("Принтер - 1")
            print("Сканер  - 2")
            print("Ксерокс - 3")
            print("Пустая строка чтобы закончить ввод.")
            in_data = input()
            if in_data in ("1", "2", "3", " "):
                if in_data == "1":
                    try:
                        param = input("Какой нужен формат принтера?: ")
                        count = int(input("Введите количество: "))
                        warehouse1.outcome_equipment("Printer", param, count)
                    except Exception as err:
                        print(err)
                if in_data == "2":
                    try:
                        param = input("Какой тип сканера нужен?: ")
                        count = int(input("Введите количество: "))
                        warehouse1.outcome_equipment("Scaner", param, count)
                    except Exception as err:
                        print(err)
                if in_data == "3":
                    try:
                        param = input("Какой размер копира нужен?: ")
                        count = int(input("Введите количество: "))
                        warehouse1.outcome_equipment("Xerox", param, count)
                    except Exception as err:
                        print(err)
                if in_data == " ":
                    break
    if in_data == "3":
        warehouse1.inventory()
    if in_data.upper() == "Q":
        break
