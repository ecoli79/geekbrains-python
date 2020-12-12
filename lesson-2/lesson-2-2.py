# Lesson-2 example 2
# working with list and cycle while by Python

my_list = list(input("Введите любые символы с клавиатуры: "))

print(f"Вы ввели {my_list}")

my_list[0:len(my_list)-1:2], my_list[1:len(my_list):2] = my_list[1:len(my_list):2], my_list[0:len(my_list)-1:2]

print(f"После некоторой магии получилось вот что: {my_list}")
