# Lesson-1 example 2
# Counting hours, minutes, seconds from input

seconds = int(input("Please, enter seconds: "))
hours = ((seconds//3600)) % 24
minutes = (seconds//60) % 60
seconds = seconds % 60

print(f"{hours:02}:{minutes:02}:{seconds:02}")
