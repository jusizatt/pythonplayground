import time

def part_2():
    #string = "X(8x2)(3x3)ABCY"
    #string = "(27x12)(20x12)(13x14)(7x10)(1x12)A"
    #string = "(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"
    string = open("C:\\W\\pythonplayground\\aoc\\2016\input\\aocDay9_input.txt", "r").read()
    print("OriginalString -- ", string)
    extractedString = extract(string)
    print(extractedString)



def extract(str):
    index = 0
    runningLength = 0
    while True:
        if index >= len(str):
            runningLength += len(str)
            break

        char = str[index]
        if char != "(":
            index += 1
            continue

        f = str.find("(", index)
        s = str.find(")", index)

        p = str[f+1:s]

        firstNum, secondNum = p.split("x")
        val = str[s+1:s+1+int(firstNum)]
        decCompressed = val * int(secondNum)
        if decCompressed.find("(") != -1:
            runningLength += len(str[:index])
            str = decCompressed + str[index+(s-f+1)+int(firstNum):]
        else:
            runningLength += len(str[:index]) + len(decCompressed)
            str = str[index+(s-f+1)+int(firstNum):]

        index = 0

    return runningLength

if __name__ == "__main__":
    start_time = time.time()
    part_2()
    current_time = time.time()
    elapsed_time = current_time - start_time
    print(elapsed_time)