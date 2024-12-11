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


def next_step(position, direct):
    next_s = []
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
    return next_s


def is_in_bounds(n_step, lab_map):
    size = lab_size(lab_map)
    if 0 > n_step[0] > size[0]:
        return True
    elif 0 > n_step[1] > size[1]:
        return True
    else:
        return False


def obstacle_in_way(n_step, lab_map):
    if lab_map[n_step[0]][n_step[1]] == '#':
        return True
    else:
        return False


# def patrol(lab_map):
#     direction = 'up'
#     places_been = []
#     bounds = True
#     position = starting_point(lab_map)
#     places_been.append(position)
#     while bounds:
#         next_s = next_step(position, direction)
#         if is_in_bounds(next_s,lab_map):
#             if obstacle_in_way(next_s, lab_map):
#                 direction = turn_right(direction)
#                 next_s


lab_raw = open("day_6_input.txt", "r")
lab = []

for l in lab_raw:
    l = l.replace("\n",'')
    lab.append(l)

# direction = 'up'

# print(lab_size(lab))
# print(starting_point(lab))