# lesson-4 example 4
# working with generators

# найти в исходном списке повторения и вывести их в отедельный список в порядке следования в исходном списке

list_in = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
list_out = [el for el in list_in if list_in.count(el) == 1]

print(list_out)
