filePath = "C:\\W\\pythonplayground\\aoc\\2015\\aoc2015_day6_input.txt"

#3https://www.educba.com/multidimensional-array-in-python/
##lightGrid = [1000][1000]

def Part1():
    f = open(filePath, "r")
    lines = f.read()
    
    print("Part 1")

def Part2():
    f = open(filePath, "r")
    lines = f.read()
  
    print("Part 2")

def turnOn(xLow, xHigh, yLow, yHigh):
    for x in range(xLow, xHigh):
      for y in range(yLow, yHigh):
        lightGrid[x][y] = 1

def turnOff(xLow, xHigh, yLow, yHigh):
    for x in range(xLow, xHigh):
      for y in range(yLow, yHigh):
        lightGrid[x][y] = 0

if __name__ == "__main__":
    turnOff(0, 999, 0, 999)
    Part1()
    Part2()