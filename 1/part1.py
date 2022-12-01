# Day 1 Part 1 - Approx time: 3 mins
# Could have split the file into different lists however couldn't be bothered with the mess and would rather do something more readable

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
