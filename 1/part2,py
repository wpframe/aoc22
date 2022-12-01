# Day 1 Part 2 - Approx time: 10 mins
# Ended up trying to iterate through the top_3 list I created using an index and then changed it which resulted in this taking a bit more time than I should have

file = open("input.txt", "r")

top_3 = [0, 0, 0]

count = 0
for line in file:
    line = line.strip("\n")
    if line == "":
        if min(top_3) < count:
            top_3[top_3.index(min(top_3))] = count
        count = 0
    else:
        count = count + int(line)
        
print(sum(top_3))
