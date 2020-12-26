# lesson 4 example 7
# working with functions and yield

def fact(num_fact):
    """Функция получения факториала числа num_fact"""

    p = 1
    for i in range(1, num_fact+1):
        p *= i
        yield p


for i in fact(15):
    print(i)
