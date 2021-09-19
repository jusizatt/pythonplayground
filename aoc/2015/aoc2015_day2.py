def Part1():
    f = open("C:\\W\\pythonplayground\\aoc\\2015\\aoc2015_day2_input.txt", "r")
    lines = f.read()
    runningTotal = 0
    for x in lines.split('\n'):
        parts = x.split('x')
        l, w, h = int(parts[0]), int(parts[1]), int(parts[2])
        minside = min(l*w, w*h, h*l)
        sum = (2 * l * w) + (2 * w * h) + (2 * h * l) + minside
        runningTotal += sum

    print("Part 1", runningTotal)

def Part2():
    f = open("C:\\W\\pythonplayground\\aoc\\2015\\aoc2015_day2_input.txt", "r")
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