# lesson 3 example 4
# working with function and arguments

def my_func_simple(x, y):
    """Возведение числа x в степень y, где x действительное положительное число, а y целое отрицательно число"""

    return x**y


def my_func_dif(x, y):
    """Возведение числа x в степень y, где x действительное положительное число, а y целое отрицательно число"""

    i = 0
    b = 1
    if y < 0:
        for i in (range(abs(y))):
            i += 1
            b *= x
    return 1 / b


try:
    while True:
        x = int(input("Введите целое положительное число: "))
        y = int(input("Введите целое отрицательное число: "))

        if x > 0 and y < 0:
            print(f"Результат выполнения по формуле x**y {my_func_dif(x, y)}")
            print(f"Результат выполнения через цикл {my_func_simple(x, y)}")


except Exception as err:
    print(err)
