# Lesson-1 example 4
# Find the bigest digint in input

dig = input("Enter any digits: ")

bigest = 0
i = 0
digits = int(dig)

while i < len(dig):

    j = digits % 10
    digits = digits // 10

    if bigest < j:
        bigest = j

    i = i + 1

print(f"The bigest number is {bigest}")
