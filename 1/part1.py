file = open("input.txt", "r") # Day 1 Part 1
max, count = 0
for line in file:
    if line.strip("\n") == "": 
        if count > max: max = count:
        count = 0
    else: count = count + int(line)
print(max)
