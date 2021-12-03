def parse():
    file = open("C:\\W\\pythonplayground\\aoc\\2021\\input\\day03_input.txt", "r")
    lines = file.read().split('\n')
    return lines

def part_one():
    lines = parse()

    for i in range(0, len(lines)):
    

if __name__ == "__main__":
  ans = part_one()
  print("Part 1...", ans)

#   ans = part_two()
#   print("Part 2...", ans)