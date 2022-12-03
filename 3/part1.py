# Day 3 Part 1

file = open("input.txt", "r")

total = 0

for line in file:
    first_half = line[:len(line) // 2]
    second_half = line[len(line) // 2:]
    common_item = ''
    for char in first_half:
        if char in second_half:
            common_item = char
    if common_item.islower():
        total += (ord(common_item) - 96)
    else:
        total += (ord(common_item) - 38)

print(total)
