
def Part1():
    f = open("C:\\W\\python\\aoc\\aoc2015_day1_input.txt", "r")
    lines = f.read()
    count = 0
    for c in iter(lines):
        if c == '(':
            count += 1
        elif c == ')':
            count -= 1
        else:
            print(c)
            assert c == '(' or c == ')', "shouldnt be here"

    print("Part 1", count)

def Part2():
    f = open("C:\\W\\python\\aoc\\aoc2015_day1_input.txt", "r")
    lines = f.read()
    count = 0
    i = 0
    for c in iter(lines):
        i+=1
        if c == '(':
            count += 1
        elif c == ')':
            count -= 1
        else:
            print(c)
            assert c == '(' or c == ')', "shouldnt be here"

        if count == -1:
            break

    print("Part 2", i)

if __name__ == "__main__":
    Part1()
    Part2()