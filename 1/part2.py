file = open("input.txt", "r") # Day 1 Part 2
top_3 = [0, 0, 0]
count = 0
for line in file:
    if line.strip("\n") == "":
        if min(top_3) < count: top_3[top_3.index(min(top_3))] = count
        count = 0
    else: count = count + int(line)
print(sum(top_3))
