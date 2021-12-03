def day1():
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

def day2():
    with open('Day2/input.txt') as i:
        x = 0
        y = 0
        X = 0
        Y = 0
        aim = 0
        for line in i:
            data = line.split()
            command = data[0]
            number = int(data[1])
            if command == 'forward':
                x += number
                X += number
                Y += number * aim
            elif command == 'down':
                y += number
                aim += number
            elif command == 'up':
                y -= number
                aim -= number
            else:
                pass
        print("Part 1")
        print(x, "x", y, "=", x*y)
        print("Part 2")
        print(X, "x", Y, "=", X*Y)

def day3():
    with open('Day3/input.txt') as i:
        gamma_list = []
        epsilon_list = []
        rowsize = 1000
        columnsize = 12
        most_common_bits = [[0] * columnsize for i in range(rowsize)]
        one = 0
        zero = 0
        k = 0
        for line in i:
            print(line)
            j = 0
            for char in line:
                if char != '\n':
                    number = int(char)
                    most_common_bits[k][j] = number
                j += 1
            k += 1    

        for y in range(12):
            for x in range(rowsize):
                if most_common_bits[x][y] == 1:
                    one += 1
                elif most_common_bits[x][y] == 0:
                    zero += 1
            if one > zero:
                gamma_list.append(1)
                epsilon_list.append(0)
            else:
                gamma_list.append(0)
                epsilon_list.append(1)
            one = 0
            zero = 0
        numbers = [str(integer) for integer in gamma_list]
        g_string = "".join(numbers)
        gamma = int(g_string, 2)
        numbers = [str(integer) for integer in epsilon_list]
        e_string = "".join(numbers)
        epsilon = int(e_string, 2)
        print(gamma, "x", epsilon, "=", gamma*epsilon)

day3()
