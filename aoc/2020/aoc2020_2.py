from fileinput import FileInput
import fileinput
from os import remove, replace

def main():
    file=open("C:/w/python/aoc2021_input.txt","r")
    # count = 0
    # for x in file.readlines():
    #     if processLine(x[:-1]):
    #         count += 1

    # print(count)

    count = 0
    for x in file.readlines():
        if processLineTwo(x[:-1]):
            count += 1

    print(count)


def processLine(line):
    print(line)
    parts = line.split(" ")
    
    middle = int(parts[0].find("-"))

    range = parts[0]
    lowerBound = int(range[:middle])
    upperBound = int(range[(middle + 1):])

    letter = parts[1][0]
    phrase = parts[2]
    count = findChars(letter, phrase)
    
    if (count >= lowerBound and count <= upperBound):
        return True

def processLineTwo(line):
    print(line)
    parts = line.split(" ")
    
    middle = int(parts[0].find("-"))

    range = parts[0]
    lowerBound = int(range[:middle])
    upperBound = int(range[(middle + 1):])

    letter = parts[1][0]
    letter1 = ''
    letter2 = ''
    if upperBound <= len(parts[2]) and upperBound > 1:
        letter1 = parts[2][upperBound - 1]

    if lowerBound <= len(parts[2]) and lowerBound > 1:
        letter2 = parts[2][lowerBound - 1]

    if (letter1 == letter or letter2 == letter):
        return True
    else:
        return False


def findChars(lookup, input):

    count = 0
    for i in input:
        if lookup == i:
            count += 1

    return count


if  __name__ == "__main__":
    main()