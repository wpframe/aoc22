# Day 3 Part 2

file = open("input.txt", "r")
lines = file.readlines()

total = 0
i = 2

while i < len(lines):
    one = lines[i - 2]
    two = lines[i - 1]
    three = lines[i]
    badge = ''
    for char in one:
        if char in two and char in three:
            badge = char
            break
    if badge.islower():
        total += (ord(badge) - 96)
    else:
        total += (ord(badge) - 38)
    i += 3

print(total)
