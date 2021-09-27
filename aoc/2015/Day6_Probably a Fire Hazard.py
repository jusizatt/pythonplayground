from os import truncate
import re

filePath = "C:\\W\\python\\aoc\\2015\\aoc2015_day6_input.txt"

#3https://www.educba.com/multidimensional-array-in-python/
c = 1000
r = 1000
lightGrid = [ [False] * c for i in range(r) ]

def Clear():
    global lightGrid
    lightGrid = [ [False] * c for i in range(r) ]

def PrintLightGrid():
    print("----------------------------------------------")

    for line in lightGrid:
        print(line)

    print("----------------------------------------------")

def DisplayLightGridCount():
    count = 0
    for line in lightGrid:
        for row in line:
            if row is True:
                count+=1
    
    print(count, "lights on.")


def Part1():
    f = open(filePath, "r")
    lines = f.read()
    
    for x in lines.split('\n'):
        if x.startswith("turn on"):
            formattedString = x.replace(" through ", " ").replace("turn on ", "")
            print("On", formattedString)
            parts = formattedString.split(" ")
            (xlow, ylow) = parts[0].split(",")
            (xhigh, yhigh) = parts[1].split(",")

            turnOn(int(xlow), int(ylow), int(xhigh), int(yhigh))

        elif x.startswith("turn off"):
            formattedString = x.replace(" through ", " ").replace("turn off ", "")
            print("Off", formattedString)
            parts = formattedString.split(" ")
            (xlow, ylow) = parts[0].split(",")
            (xhigh, yhigh) = parts[1].split(",")
            
            turnOff(int(xlow), int(ylow), int(xhigh), int(yhigh))

        else:
            formattedString = x.replace(" through ", " ").replace("toggle ", "")
            print("toggle", formattedString)
            parts = formattedString.split(" ")
            (xlow, ylow) = parts[0].split(",")
            (xhigh, yhigh) = parts[1].split(",")
            
            toggle(int(xlow), int(ylow), int(xhigh), int(yhigh))

    print("Part 1")

def Part2():
    f = open(filePath, "r")
    lines = f.read()
  
    print("Part 2")

def turnOn(xLow, xHigh, yLow, yHigh):
    for x in range(xLow, xHigh + 1):
      for y in range(yLow, yHigh + 1):
        lightGrid[x][y] = True

def turnOff(xLow, xHigh, yLow, yHigh):
    for x in range(xLow, xHigh + 1):
      for y in range(yLow, yHigh + 1):
        lightGrid[x][y] = False

def toggle(xLow, xHigh, yLow, yHigh):
    for x in range(xLow, xHigh + 1):
      for y in range(yLow, yHigh + 1):
        lightGrid[x][y] = not lightGrid[x][y]

if __name__ == "__main__":
    print("Starting Program...")

    # turnOn(499, 500, 499, 500)
    # DisplayLightGridCount()
    # turnOff(499, 500, 499, 500)
    # DisplayLightGridCount()
    # toggle(499, 500, 499, 500)
    # DisplayLightGridCount()
    # Clear()
    # turnOn(0, 999, 0, 999)
    # DisplayLightGridCount()
    # Clear()

    Part1()
    DisplayLightGridCount()
    Clear()
    

    Part2()