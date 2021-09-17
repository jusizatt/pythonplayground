def Part1():
    f = open("C:\\W\\python\\aoc\\aoc2015_day2_input.txt", "r")
    lines = f.read()
    
    print("Part 1")

def Part2():
    f = open("C:\\W\\python\\aoc\\aoc2015_day2_input.txt", "r")
    lines = f.read()
    order = 0
    for l in lines.split('\n'):
        parts = l.split('x')
        order += calculateDimentions(parts[0], parts[1], parts[2])

    print("Part 2", order)

def calculateDimentions(one, two, three):
    l = [int(one), int(two), int(three)]
    l.sort()

    runningTotal = 0
    runningTotal += l[0] + l[0]
    runningTotal += l[1] + l[1]
    
    runningTotal += (l[0] * l[1] * l[2])
    return runningTotal


if __name__ == "__main__":
    Part1()
    Part2()