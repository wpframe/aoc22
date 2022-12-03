# Day 1 Part 1

file = open("input.txt", "r")

max = 0

count = 0
for line in file:
    line = line.strip("\n")
    if line == "":
        if count > max:
            max = count
        count = 0
    else:
        count = count + int(line)
        
print(max)
