# Advent of Code 2024 - Day 5
# ***** TASK - 1 *****


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