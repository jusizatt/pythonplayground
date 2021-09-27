from os import truncate
import re

filePath = "C:\\W\\python\\aoc\\2015\\aoc2015_day6_input.txt"

#3https://www.educba.com/multidimensional-array-in-python/

c = 1000
r = 1000
lightGrid = [ [0] * c for i in range(r) ]

def Clear():
    global lightGrid
    lightGrid = [ [0] * c for i in range(r) ]

def PrintLightGrid():
    print("----------------------------------------------")

    for line in lightGrid:
        print(line)

    print("----------------------------------------------")

def DisplayLightGridCount():
    count = 0
    for line in lightGrid:
        for row in line:
            if row is 1:
                count+=1
    
    print(count, "lights on.")

def DisplayLightGridBrightness():
    count = 0
    for x in range(0, 1000):
      for y in range(0, 1000):
        count += lightGrid[x][y]
    
    print("Total brightness:", count)


def Part1():
    f = open(filePath, "r")
    lines = f.read()
    
    for x in lines.split('\n'):
        if x.startswith("turn on"):
            formattedString = x.replace(" through ", " ").replace("turn on ", "")
            parts = formattedString.split(" ")
            (xlow, ylow) = parts[0].split(",")
            (xhigh, yhigh) = parts[1].split(",")

            turnOn(int(xlow), int(ylow), int(xhigh), int(yhigh))

        elif x.startswith("turn off"):
            formattedString = x.replace(" through ", " ").replace("turn off ", "")
            parts = formattedString.split(" ")
            (xlow, ylow) = parts[0].split(",")
            (xhigh, yhigh) = parts[1].split(",")
            
            turnOff(int(xlow), int(ylow), int(xhigh), int(yhigh))

        elif x.startswith("toggle"):
            formattedString = x.replace(" through ", " ").replace("toggle ", "")
            parts = formattedString.split(" ")
            (xlow, ylow) = parts[0].split(",")
            (xhigh, yhigh) = parts[1].split(",")
            
            toggle(int(xlow), int(ylow), int(xhigh), int(yhigh))
        
        else:
          print("BAD STUFF........................................................")

    print("Part 1")

def Part2():
    f = open(filePath, "r")
    lines = f.read()
    
    for x in lines.split('\n'):
        if x.startswith("turn on"):
            formattedString = x.replace(" through ", " ").replace("turn on ", "")
            parts = formattedString.split(" ")
            (xlow, ylow) = parts[0].split(",")
            (xhigh, yhigh) = parts[1].split(",")

            turnBrighnessUp(int(xlow), int(ylow), int(xhigh), int(yhigh))

        elif x.startswith("turn off"):
            formattedString = x.replace(" through ", " ").replace("turn off ", "")
            parts = formattedString.split(" ")
            (xlow, ylow) = parts[0].split(",")
            (xhigh, yhigh) = parts[1].split(",")
            
            turnBrightnessDown(int(xlow), int(ylow), int(xhigh), int(yhigh))

        elif x.startswith("toggle"):
            formattedString = x.replace(" through ", " ").replace("toggle ", "")
            parts = formattedString.split(" ")
            (xlow, ylow) = parts[0].split(",")
            (xhigh, yhigh) = parts[1].split(",")
            
            turnBrightnessUp_2(int(xlow), int(ylow), int(xhigh), int(yhigh))
        
        else:
          print("BAD STUFF........................................................")
  
    print("Part 2")

def turnOn(x1, y1, x2, y2):
    for x in range(x1, x2 + 1):
      for y in range(y1, y2 + 1):
        lightGrid[x][y] = 1

def turnOff(x1, y1, x2, y2):
    for x in range(x1, x2 + 1):
      for y in range(y1, y2 + 1):
        lightGrid[x][y] = 0

def toggle(x1, y1, x2, y2):
    for x in range(x1, x2 + 1):
      for y in range(y1, y2 + 1):
        lightGrid[x][y] = 1 if lightGrid[x][y] == 0 else 0

def turnBrighnessUp(x1, y1, x2, y2):
    for x in range(x1, x2 + 1):
      for y in range(y1, y2 + 1):
        lightGrid[x][y] = lightGrid[x][y] + 1

def turnBrightnessDown(x1, y1, x2, y2):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if lightGrid[x][y] == 0:
                continue

            lightGrid[x][y] = lightGrid[x][y] - 1

def turnBrightnessUp_2(x1, y1, x2, y2):
    for x in range(x1, x2 + 1):
      for y in range(y1, y2 + 1):
        lightGrid[x][y] = lightGrid[x][y] + 2

if __name__ == "__main__":
    print("Starting Program...")

    Part1()
    DisplayLightGridCount()
    Clear()

    # Part 2 Test Data
    # turnBrighnessUp(0,0, 0,0)
    # turnBrighnessUp(0,0, 0,0)
    # turnBrighnessUp(0,0, 0,0)
    # DisplayLightGridBrightness()
    # Clear()
    # turnBrightnessUp_2(0,0, 999,999)
    # DisplayLightGridBrightness()
    # Clear()

    Part2()
    DisplayLightGridBrightness()
