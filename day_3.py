# Advent of Code 2024 - Day 3
# Task 1
import regex

input_data = open("day_3_input.txt", "r")
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
total = 0
for i in input_data:
    multiplications = regex.findall(pattern, i)
    for multiplication in multiplications:
        score = int(multiplication[0]) * int(multiplication[1])
        total += score

print(f'Task 1 - {total}')

