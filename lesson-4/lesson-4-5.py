# lesson-4 example 5
# working with geretator and reduce()

# получить список с четными числами от 100 до 1000 включительно, и получить результат воспроизведения всех чисел.
# Используем встроенную функцию reduce() для упрощения обхода последовательности

from functools import reduce


def multipule(par1, par2):

    return par1 * par2


list_in = [el for el in range(100, 1001) if el % 2 == 0]

print(reduce(multipule, list_in))
