# lesson-4 example 2
# working with generators

my_list = [12, 14, 45, 65, 23, 85, 102, 228, 12, 22, 43]
new_list = [el for el in my_list if el > my_list[my_list.index(el) - 1]]

print(new_list)
