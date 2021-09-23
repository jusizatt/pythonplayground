import re

filePath = "C:\\W\\python\\aoc\\2015\\aoc2015_day6_input.txt"

#3https://www.educba.com/multidimensional-array-in-python/
c = 1000
r = 1000
lightGrid = [ [False] * c for i in range(r) ]

def Part1():
    f = open(filePath, "r")
    lines = f.read()
    
    for x in lines.split('\n'):
        stuff = re.search("(turn on|toggle|turn off)\ (\d+)\,(\d+)\ through\ (\d+)\,(\d+)", x)
        print(stuff)

    print("Part 1")

def Part2():
    f = open(filePath, "r")
    lines = f.read()
  
    print("Part 2")

def turnOn(xLow, xHigh, yLow, yHigh):
    for x in range(xLow, xHigh):
      for y in range(yLow, yHigh):
        lightGrid[x][y] = True

def turnOff(xLow, xHigh, yLow, yHigh):
    for x in range(xLow, xHigh):
      for y in range(yLow, yHigh):
        lightGrid[x][y] = False

if __name__ == "__main__":
    ##turnOff(0, 999, 0, 999)
    Part1()
    Part2()