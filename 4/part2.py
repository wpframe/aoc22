# Day 3 Part 2

file = open("input.txt", "r")

count = 0

for line in file:
    line = line.split(",")
    list1 = line[0].split("-")
    list2 = line[1].strip("\n").split("-")
    range1 = range(int(list1[0]), int(list1[1]) + 1)
    range2 = range(int(list2[0]), int(list2[1]) + 1)
    for i in range1:
        if i in range2:
            count += 1
            break

print(count)