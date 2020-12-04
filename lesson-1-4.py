# Lesson-1 example 4
# Find the bigest digint in input

dig = input("Enter any digits: ")

bigest = 0
i = 0

while i < len(dig):
    for each in dig:
        if int(each) > bigest:
            bigest = int(each)

    i = i + 1

print(f"The bigest number is {bigest}")
