# Advent of Code 2024 - Day 2
# Task 1

input_data = open("day_2_input.txt", "r")
safe_reports = 0
unsafe_levels = []

for i in input_data:
    i = i.replace('\n', '')
    i = i.split()
    for j in range(len(i)):
        i[j] = int(i[j])

    safe = True

    if i[0] > i[1]:
        for k in range(len(i) - 1):
            decrease_rate = i[k] - i[k+1]
            if 0 >= decrease_rate or decrease_rate > 3:
                safe = False

    elif i[0] < i[1]:
        for k in range(len(i) - 1):
            increase_rate = i[k] - i[k+1]
            if 0 <= increase_rate or increase_rate < -3:
                safe = False
    else:
        safe = False

    if safe:
        safe_reports += 1
    else:
        unsafe_levels.append(i)

print(f"Task 1: {safe_reports}")

# Task 2

for u in unsafe_levels:
    print(u)
