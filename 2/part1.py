# Day 2 Part 1

file = open("input.txt", "r")

win_pairs = [["X", "C"],["Y", "A"],["Z", "B"]]
pairs = [["X", "A"],["Y", "B"],["Z", "C"]]

score = 0

for line in file:
    for pair in win_pairs:
        if line[0] in pair and line[2] in pair:
            score += 6
    if line[2] == 'X':
        score += 1
    if line[2] == 'Y':
        score += 2
    if line[2] == 'Z':
        score += 3
    for pair in pairs:
        if line[0] in pair and line[2] in pair:
            score += 3
print(score)
