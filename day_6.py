# Advent of Code 2024 - Day 6
# ***** TASK - 1 *****


def lab_size(lab_map):
    x = len(lab_map)
    y = len(lab_map[0])
    return [x,y]


def starting_point(lab_map):
    size = lab_size(lab_map)
    for x in range(size[0]):
        for y in range(size[1]):
            if lab_map[x][y] == '^':
                return [x,y]


def turn_right(direct):
    if direct == 'up':
        direct = 'right'
    elif direct == 'right':
        direct = 'down'
    elif direct == 'down':
        direct = 'left'
    elif direct == 'left':
        direct = 'up'
    return direct


def what_direction(position, n_step):
    if position[0] > n_step[0]:
        direct = 'up'
    elif position[0] < n_step[0]:
        direct = 'down'
    elif position[1] > n_step[1]:
        direct = 'left'
    elif position[1] < n_step[1]:
        direct = 'right'
    return direct


def obstacle_in_way(n_step, lab_map):
    if lab_map[n_step[0]][n_step[1]] == '#':
        return True
    else:
        return False


def next_step(position, direct, lab_map):
    next_s = [0,0]
    if direct == 'up':
        next_s[0] = position[0] - 1
        next_s[1] = position[1]
    elif direct == 'right':
        next_s[0] = position[0]
        next_s[1] = position[1] + 1
    elif direct == 'down':
        next_s[0] = position[0] + 1
        next_s[1] = position[1]
    elif direct == 'left':
        next_s[0] = position[0]
        next_s[1] = position[1] - 1
    if obstacle_in_way(next_s, lab_map):
        direct = turn_right(direct)
        next_s = next_step(position, direct, lab_map)
    return next_s


def is_in_bounds(n_step, lab_map):
    size = lab_size(lab_map)
    if 0 > n_step[0] or n_step[0] > size[0]:
        return False
    if 0 > n_step[1] or n_step[1] > size[1]:
        return False
    return True


def patrol(lab_map):
    direction = 'up'
    places_been = []
    bounds = True
    position = starting_point(lab_map)
    while bounds:
        next_s = next_step(position, direction, lab_map)
        direction = what_direction(position, next_s)
        places_been.append(position)
        print(position)
        position = next_s
        if not is_in_bounds(next_s, lab_map):
            bounds = False
    return places_been


lab_raw = open("day_6_input.txt", "r")
lab = []

for l in lab_raw:
    l = l.replace("\n",'')
    lab.append(l)

score = patrol(lab)
print(len(score))
unique_data = [list(x) for x in set(tuple(x) for x in score)]
print(len(unique_data))