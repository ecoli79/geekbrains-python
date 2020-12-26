# lesson-4 example 3
# working with generators

# ищем числа кратные 20 или 21 в диапозоне от 20 до 240
my_list = [el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]

print(my_list)
