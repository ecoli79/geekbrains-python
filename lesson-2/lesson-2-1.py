# Lesson-2 example 1
# working with type of data by Python

my_list = [True, None, "строка", 7.23, 16, [1, 2, 3],
           (3, 2, 1), {4, 5, 6}, dict(раз='1', два='2')]

print(f"Переднами список элементов: {my_list}")
print("Вот типы данных представленных в этом списке: ")

for each in my_list:
    print(str(each) + " - " + str(type(each)))
