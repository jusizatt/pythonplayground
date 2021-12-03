def parse():
    file = open("C:\\W\\pythonplayground\\aoc\\2021\\input\\day02_input.txt", "r")
    lines = file.read().split('\n')
    return lines

def part_one():
    lines = parse()

    forward = 0
    vertical = 0

    for i in range(0, len(lines)):
        line = lines[i]
        print(line)
        value = int(line.split(" ")[1])
        if line.find("forward ") >= 0:
            forward += value
        
        if line.find("up ") >= 0:
            vertical -= value
        
        if line.find("down ") >= 0:
            vertical += value
        
        print("positioni", forward, vertical)

    return forward * vertical

def part_two():
    lines = parse()

    aim = 0
    forward = 0
    vertical = 0

    for i in range(0, len(lines)):
        line = lines[i]
        print(line)
        value = int(line.split(" ")[1])
        if line.find("forward ") >= 0:
            forward += value
            vertical += aim * value
        
        if line.find("up ") >= 0:
            ##vertical -= value
            aim -=value
        
        if line.find("down ") >= 0:
            ##vertical += value
            aim += value
        
        print("positioni", forward, vertical)

    return forward * vertical

if __name__ == "__main__":
  ans = part_one()
  print("Part 1...", ans)

  ans = part_two()
  print("Part 2...", ans)