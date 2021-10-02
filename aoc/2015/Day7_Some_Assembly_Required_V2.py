from os import error
# not 65535

filePath = "C:\\W\\python\\aoc\\2015\\aoc2015_day7_input.txt"

wires = {}
wireValues = {}

def parseInput(line):
    i = str(line).index(" -> ")
    wires[line[i + 4:]] = line[:i]
    print(line)
    
    firstValue = line.split(" ")[0]
    lastValue = line.split(" ")[-1]

    if firstValue.isdigit():
        wireValues[lastValue] = int(firstValue)


def Part1():
    f = open(filePath, "r")
    lines = f.read()
    for l in lines.split('\n'):
        parseInput(l)
    
    val = recursiveLookup("a")
    print("-----------------------------------------------\n", "a = ", val)

    # for k, v in wires.items():
    #     val = recursiveLookup(k)
    #     if val is not None:
    #         wireValues[k] = val

def recursiveLookup(key):
    opperator = wires[key]
    print(key)
    print(opperator)
    if opperator.find("NOT") == 0:
        parts = opperator.split(" ")
        r = 0
        if parts[1].isdigit():
            return int(r)
        else:
           r = wireValues[parts[1]] if wireValues.get(parts[1], None) is not None else recursiveLookup(parts[0])

        op = invert_bits(r, 16)
        wireValues[key] = op
        return op  

    elif opperator.find("RSHIFT") > 1:
        parts = opperator.split(" ")

        l = 0
        r = 0
        if not parts[0].isdigit():
            l = wireValues[parts[0]] if wireValues.get(parts[0], None) is not None else recursiveLookup(parts[0])
        else:
            l = int(parts[0])

        if not parts[2].isdigit():
            r = wireValues[parts[2]] if wireValues.get(parts[2], None) is not None else recursiveLookup(parts[2])
        else:
            r = int(parts[2])

        op = l >> r
        wireValues[key] = op
        return op   

    elif opperator.find("LSHIFT") > 1:
        parts = opperator.split(" ")
        l = 0
        r = 0
        if not parts[0].isdigit():
            l = wireValues[parts[0]] if wireValues.get(parts[0], None) is not None else recursiveLookup(parts[0])
        else:
            l = int(parts[0])

        if not parts[2].isdigit():
            r = wireValues[parts[2]] if wireValues.get(parts[2], None) is not None else recursiveLookup(parts[2])
        else:
            r = int(parts[2])

        op = l << r
        wireValues[key] = op
        return op   

    elif opperator.find("AND") > 1:
        parts = opperator.split(" ")
        
        l = 0
        r = 0
        if not parts[0].isdigit():
            l = wireValues[parts[0]] if wireValues.get(parts[0], None) is not None else recursiveLookup(parts[0])
        else:
            l = int(parts[0])

        if not parts[2].isdigit():
            r = wireValues[parts[2]] if wireValues.get(parts[2], None) is not None else recursiveLookup(parts[2])
        else:
            r = int(parts[2])

        op = l & r   
        wireValues[key] = op
        return op  

    elif opperator.find("OR") > 1:
        parts = opperator.split(" ")
        
        l = 0
        r = 0
        if not parts[0].isdigit():
            l = wireValues[parts[0]] if wireValues.get(parts[0], None) is not None else recursiveLookup(parts[0])
        else:
            l = int(parts[0])

        if not parts[2].isdigit():
            r = wireValues[parts[2]] if wireValues.get(parts[2], None) is not None else recursiveLookup(parts[2])
        else:
            r = int(parts[2])

        op =  l | r 
        wireValues[key] = op
        return op

    else:
        if opperator.isdigit():
            return int(opperator)
        elif type(opperator) is str:
            return recursiveLookup(opperator)

def Part2():
    f = open(filePath, "r")
    lines = f.read()

def invert_bits(x, numBits):
    if x < 0:
        raise ValueError("Error")
    complement = ~x
    inverted = complement + (1 << numBits)
    if inverted < 0:
        raise ValueError("Error")
    
    return inverted

if __name__ == "__main__":
    print("Starting Program...")

    Part1()
    #Part2()