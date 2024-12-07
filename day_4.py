# Advent of Code 2024 - Day 4
# Task 1

input_data = open("day_4_input.txt", "r")
word_puzzle = []
for i in input_data:
    i = i.replace('\n', '')
    word_puzzle.append(i)

word_count = 0
for x in range(len(word_puzzle)):
    for y in range(len(word_puzzle[x])):
        if word_puzzle[x][y] == 'X':
            # Horizontal search
            if y < len(word_puzzle[x]) - 3:
                if word_puzzle[x][y+1] == 'M' and word_puzzle[x][y+2] == 'A' and word_puzzle[x][y+3] == 'S':
                    word_count += 1
            # Backwards horizontal
            if y > 2:
                if word_puzzle[x][y-1] == 'M' and word_puzzle[x][y-2] == 'A' and word_puzzle[x][y-3] == 'S':
                    word_count += 1
            # Vertical search
            if x < len(word_puzzle) - 3:
                if word_puzzle[x+1][y] == 'M' and word_puzzle[x+2][y] == 'A' and word_puzzle[x+3][y] == 'S':
                    word_count += 1
            # Backwards vertical
            if x > 2:
                if word_puzzle[x-1][y] == 'M' and word_puzzle[x-2][y] == 'A' and word_puzzle[x-3][y] == 'S':
                    word_count += 1
            # Diagonal up left
            if x > 2 and y > 2:
                if word_puzzle[x-1][y-1] == 'M' and word_puzzle[x-2][y-2] == 'A' and word_puzzle[x-3][y-3] == 'S':
                    word_count += 1
            # Diagonal up right
            if x > 2 and y < len(word_puzzle[x]) - 3:
                if word_puzzle[x-1][y+1] == 'M' and word_puzzle[x-2][y+2] == 'A' and word_puzzle[x-3][y+3] == 'S':
                    word_count += 1
            # Diagonal down right
            if x < len(word_puzzle) - 3 and y < len(word_puzzle[x]) - 3:
                if word_puzzle[x+1][y+1] == 'M' and word_puzzle[x+2][y+2] == 'A' and word_puzzle[x+3][y+3] == 'S':
                    word_count += 1
            # Diagonal down left
            if x < len(word_puzzle) - 3 and y > 2:
                if word_puzzle[x+1][y-1] == 'M' and word_puzzle[x+2][y-2] == 'A' and word_puzzle[x+3][y-3] == 'S':
                    word_count += 1
print(f"Task 1: {word_count}")

