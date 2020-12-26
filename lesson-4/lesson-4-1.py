# lesson-4 example 1
# working with parameters throw terminal

from sys import argv

try:
    def sallury_count(hours, rate, bonus):
        """Разчет заработной платы сотрудника
        hourse - отработанные часы за месяц по табелю
        rate   - ставка сотрудника (оклад)
        bonus  - премия, если премии нет то 0
        """
        try:
            sallury_summ = (int(hours) * int(rate)) + int(bonus)
            return sallury_summ
        except:
            return "Вы не предоставили не корректные данные."

    name_module, hours, rate, bonus = argv
    sallary_itog = sallury_count(hours, rate, bonus)
    print(f"Заработная плата сотрудника составляет - {sallary_itog} рублей")

except:
    print("Для расчета заработной платы сотрудника необходимо ввести данные - количество отработанных часов, стоимость часа работы и сумму преимии (если премии нет, ввести 0). Например: 220 1200 0")
