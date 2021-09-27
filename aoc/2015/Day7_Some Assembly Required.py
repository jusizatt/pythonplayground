filePath = "C:\\W\\python\\aoc\\2015\\aoc2015_day7_input.txt"

wires = {}
wireValues = {}

def parseInput(line):
    i = str(line).index(" -> ")
    wires[line[i + 4:]] = line[:i]
    print(wires)


def Part1():
    f = open(filePath, "r")
    lines = f.read()
    for l in lines.split('\n'):
        parseInput(l)

    for k, v in wires.items():
        wires[k] = recursiveLookup(v)

def recursiveLookup(opperator):
    if opperator.Contains("NOT"):
       dicKey = opperator[3:]
       dicVal = wires[dicKey]
       isdig = dicVal.isdigit()
       if isdig:
           return isdig
       else:
           return recursiveLookup(dicVal)


def Part2():
    f = open(filePath, "r")
    lines = f.read()

    #print(lines)

if __name__ == "__main__":
    print("Starting Program...")
    Part1()
    Part2()