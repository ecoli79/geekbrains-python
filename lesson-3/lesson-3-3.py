# lesson 3 example 3
# working with function

def my_func(val_1, val_2, val_3):
    """The function input 3 argument and output summ two most values"""

    values = [val_1, val_2, val_3]
    values.sort(reverse=True)

    print(values[0] + values[1])


my_func(43, 5, 2)
