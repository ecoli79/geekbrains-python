# Lesson-1 example 3
# Summary numbers input user

dig = input("Enter any digital: ")

if dig.isdigit():

    print(int(dig) + int(dig+dig) + int(dig+dig+dig))

else:

    print("You write not digital!")
