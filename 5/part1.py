# Day 5 Part 1

file = open("input.txt", "r")
file = file.read().split("\n")

list = [[], [], [], [], [], [], [], [], []]

for line in file[:8]:
    stack_num = 0
    i = 4
    while(i < len(line) + 4):
        if "   " not in line[i-4:i]:
            list[stack_num].insert(0, line[i - 3])
        stack_num += 1
        i += 4
for line in file[10:]:
    movement = line.split(" ")
    for i in range(0, int(movement[1])):
        temp = list[int(movement[3]) - 1].pop()
        list[int(movement[5]) - 1].append(temp)

answer = ""
for stack in list:
    answer += stack[-1]

print(answer)