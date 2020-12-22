# lesson-6 example 3
# working with class

class Worker():

    """
    name - имя работника, обязательный атрибут
    surname - фамилия работника, обязательный атрибут
    position - должность работника, обязательный атрибут
    income - доход работника (заработная плата), обязательный атрибут
    """

    name = ""
    surname = ""
    position = ""
    __income = {}


class Position(Worker):

    def __init__(self, name, surname, wage, bonus):

        self.name = name
        self.surname = surname
        self.__income = {wage: float(wage), bonus: float(bonus)}

    def get_full_name(self):
        """
        получение полного имени работника
        """
        print(f"{self.surname} {self.name}")

    def get_total_income(self):
        """
        получение полного ежемесячного дохода сотрудника
        """

        print(
            f"Полный доход сотрудника в месяц составляет: {sum(self.__income.values())}")


employ = Position("Иван", "Иванов", 35000, 25000)
employ.get_full_name()
employ.get_total_income()
