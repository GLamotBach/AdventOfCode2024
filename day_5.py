# Advent of Code 2024 - Day 5
# ***** TASK - 1 *****
incorrect_lines = []


def middle_number(updte):
    m_number = updte[len(updte) // 2]
    return m_number


def check_order(update_line, rule_set):
    violations = 0
    for i in range(len(update_line)):
        previous_pages = update_line[:i]
        for r in rule_set:
            if r[0] == update_line[i]:
                if r[1] in previous_pages:
                    violations += 1
    if violations == 0:
        return middle_number(update_line)
    else:
        incorrect_lines.append(update_line)
        return 0


rules_raw = open("day_5_input_a.txt", "r")
rules = []
for rule in rules_raw:
    rule = rule.replace("\n",'')
    rule = rule.split('|')
    rule[0] = int(rule[0])
    rule[1] = int(rule[1])
    rules.append(rule)

updates_raw = open("day_5_input_b.txt", "r")
updates = []
for update in updates_raw:
    update = update.replace("\n", '')
    update = update.split(',')
    update_int = []
    for u in update:
        update_int.append(int(u))
    update = update_int
    updates.append(update)

score = 0
for u in updates:
    score += check_order(u, rules)

print(f"Task 1: {score}")

# ***** TASK - 2 *****


def sort_update(update_line, rule_set):
    for i in range(len(update_line)):
        previous_pages = update_line[:i]
        for r in rule_set:
            if r[0] == update_line[i]:
                if r[1] in previous_pages:
                    update_line[i-1], update_line[i] = update_line[i], update_line[i-1]
                    update_line = sort_update(update_line, rule_set)
    return update_line


def update_fixer(update_lines, rule_set):
    score_task_2 = 0
    for update_line in update_lines:
        score_task_2 += middle_number(sort_update(update_line,rule_set))
    return score_task_2


print(f"Task 2: {update_fixer(incorrect_lines, rules)}")