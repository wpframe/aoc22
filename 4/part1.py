# Day 3 Part 1

file = open("input.txt", "r")

count = 0

for line in file:
    line = line.split(",")
    list1 = line[0].split("-")
    list2 = line[1].strip("\n").split("-")
    set1 = set(range(int(list1[0]), int(list1[1]) + 1))
    set2 = set(range(int(list2[0]), int(list2[1]) + 1))
    if set1.issubset(set2) or set2.issubset(set1):
        count += 1

print(count)