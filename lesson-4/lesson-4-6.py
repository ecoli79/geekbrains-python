# lesson-4 example 6
# working with generators functions module itertools

from itertools import count, cycle

# Создаем генератор целых чисел с помощью count()

for num_gen in count(3):
    if num_gen > 10:
        break
    else:
        print(num_gen)

# Создаем последовательности списка с помощью итератора cycle()

trademarks = ("Mersedes", "BMW", "Peugeot", "Renault")

item = 0

for mark in cycle(trademarks):
    if item > 7:
        break
    else:
        print(mark)
        item += 1
