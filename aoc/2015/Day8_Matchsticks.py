import re

def Part1():
    f = open("C:\\W\\python\\aoc\\2015\\input\\aoc2015_day8_input.txt", "r")
    lines = f.read()
    count = 0
    for l in lines:
        count += lineCount(l)

    print("Part 1")

def Part2():
    f = open("C:\\W\\python\\aoc\\2015\\input\\aoc2015_day8_input.txt", "r")
    lines = f.read()
    
    print("Part 2")

def lineCount(line):
    print(line)
    lineLength = len(line)
    return lineLength


if __name__ == "__main__":
    p = re.compile("[\\][xX][0-9a-fA-F]{2}")
    g = p.groups
    m = p.match("\x11abc\x12abc")
    s = re.search("[\\][xX][0-9a-fA-F]{2}", "\x11abc\x12abc")
    a = re.finditer("[\\][xX][0-9a-fA-F]{2}", "\x11abc\x12abc")
    b = re.findall("[\\][xX][0-9a-fA-F]{2}", "\x11abc\x12abc")
    c = re.fullmatch("[\\][xX][0-9a-fA-F]{2}", "\x11abc\x12abc")
    d = re.match("[\\][xX][0-9a-fA-F]{2}", "\x11abc\x12abc")
    print(a)
    print(b)
    print(c)
    print(d)
    print(s)
    print(m)
    print(p)
    print(g)
    replacement = p.sub("*", "abc\x1fabc")
    print(replacement)


    #Part1()
    #Part2()