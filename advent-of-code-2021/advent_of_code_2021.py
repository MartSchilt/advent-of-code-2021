print("Day 1:")
print("Part 1")
with open('Day1/input.txt') as i:
    pn = None
    count = 0
    size = 0
    for line in i:
        n = int(line)
        size += 1
        if pn != None:
            if pn < n:
                count += 1
        pn = n
    print("Number of measurements larger than the previous measurement:", count)

print("Part 2")
with open('Day1/input.txt') as i:
    lines = i.readlines()
    j = 0
    ps = None
    count = 0
    while j < size:
        if j >= 2:
            sum = int(lines[j]) + int(lines[j-1]) + int(lines[j-2])
            if ps != None:
                if ps < sum:
                    count += 1
            ps = sum
        j += 1
    print(count)