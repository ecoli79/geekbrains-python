# Lesson-1 example 6
# working with cycles


start_result = int(input("Введите начальный результат спортсмена в км.: "))
end_result = int(
    input("Введите цель, конечный результат для достижения в км.: "))
day_of_end = 1

if end_result > start_result:

    while start_result < end_result:

        start_result = start_result * 1.1
        day_of_end = day_of_end + 1

print(
    f"Ответ: на {day_of_end}-й день спортсмен достигнет результата - не менее {end_result} км.")
