# Lesson-2 example 4
# working with string and numerable list by Python

my_str = input("Введите несколько слов с клавиатуры разделяя их пробелами: ")

for ind, el in enumerate(my_str.split()):
    print(ind, el[0:10])
