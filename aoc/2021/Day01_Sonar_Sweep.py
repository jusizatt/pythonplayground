def parse():
    file = open("C:\\W\\pythonplayground\\aoc\\2021\\input\\day01_input.txt", "r")
    #file = open("C:\\W\\python\\aoc\\2017\\input\\aoc2017_day7_input_test.txt", "r")
    lines = file.read().split('\n')
    return lines

def part_one():
    lines = parse()
    count = 0

    for i in range(0, len(lines) - 1):
        if int(lines[i]) < int(lines[i+1]):
            count += 1
    
    return count

def part_two():
    lines = parse()
    count = 0

    for i in range(0, len(lines) - 3):
        window1 = int(lines[i]) + int(lines[i + 1]) + int(lines[i + 2])
        window2 = int(lines[i+1]) + int(lines[i + 2]) + int(lines[i + 3])

        print("compare", window1, window2)

        if window1 < window2:
            count += 1
    
    return count

if __name__ == "__main__":
  count = part_one()
  print("Part 1...", count)

  count = part_two()
  print("Part 2...", count)