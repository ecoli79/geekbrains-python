# lesson 3 example 6
# working with function and agruments


def int_func(my_str):
    """Function for working string"""

    string_out = ""
    list_words = my_str.split()
    list_words = [str(el).capitalize() for el in list_words]
    for el in list_words:
        string_out += str(el) + " "

    print(string_out)


while True:
    int_func(input("Введите слово или несколько слов разделяя их пробелом: "))
