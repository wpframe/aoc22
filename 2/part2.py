#Day 2 Part 2

file = open("input.txt", "r")

win_pairs = [["X", "C"],["Y", "A"],["Z", "B"]]
loss_pairs = [["X", "B"],["Y", "C"],["Z", "A"]]
pairs = [["X", "A"],["Y", "B"],["Z", "C"]]

score = 0

for line in file:
    response = ''
    if line[2] == 'X':
        for pair in loss_pairs:
            if line[0] in pair:
                response = pair[0]
    if line[2] == 'Y':
        for pair in pairs:
            if line[0] in pair:
                response = pair[0]
    if line[2] == 'Z':
        for pair in win_pairs:
            if line[0] in pair:
                response = pair[0]
    for pair in win_pairs:
        if line[0] in pair and response in pair:
            score += 6
    if response == 'X': score += 1
    if response == 'Y': score += 2
    if response == 'Z': score += 3
    for pair in pairs:
        if line[0] in pair and response in pair:
            score += 3
print(score)
