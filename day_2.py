# Advent of Code 2024 - Day 2
# Task 1

def validate_report(report):
    if report[0] > report[1]:
        for level in range(len(report) - 1):
            decrease_rate = report[level] - report[level+1]
            if 0 >= decrease_rate or decrease_rate > 3:
                return False
    elif report[0] < report[1]:
        for level in range(len(report) - 1):
            increase_rate = report[level] - report[level+1]
            if 0 <= increase_rate or increase_rate < -3:
                return False
    else:
        return False
    return True


input_data = open("day_2_input.txt", "r")
safe_reports = 0
unsafe_reports = []

for i in input_data:
    i = i.replace('\n', '')
    i = i.split()
    for j in range(len(i)):
        i[j] = int(i[j])

    if validate_report(i):
        safe_reports += 1
    else:
        unsafe_reports.append(i)

print(f"Task 1: {safe_reports}")

# Task 2


def problem_dampener(report):
    fixed = False
    for i in range(len(report)):
        dampened_report = report.copy()
        del dampened_report[i]
        if validate_report(dampened_report):
            fixed = True
    return fixed


fixed_reports = 0
for u in unsafe_reports:
    if problem_dampener(u):
        fixed_reports += 1

print(f"Task 2: Reports fixed: {fixed_reports}, All safe reports: {safe_reports + fixed_reports}")
