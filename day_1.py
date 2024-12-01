# Advent of Code 2024 - Day 1
# Task 1

input_data = open("day_1_input.txt", "r")
list_a = []
list_b = []
score = 0

for i in input_data:
    i = i.replace('\n', '')
    i = i.split()
    list_a.append(int(i[0]))
    list_b.append(int(i[1]))

list_a.sort()
list_b.sort()

for j in range(len(list_a)):
    distance = abs(list_a[j] - list_b[j])
    score += distance

print(f"Score for first task: {score}")

# Task 2:
similarity_score = 0
for l_a in list_a:
    instance_count = 0
    for l_b in list_b:
        if l_b == l_a:
            instance_count += 1
    similarity_score += l_a * instance_count

print(f"Score for second task: {similarity_score}")



