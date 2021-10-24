def partOne():
    f = open("C:\\W\\pythonplayground\\aoc\\2016\input\\aocday7_input.txt", "r")
    lines = f.read()

    list = []
    for l in lines.split("\n"):
        print(l)
        isValid = matchOutsideBrackets(l)
        print("a[]a", isValid)
        isNotValid = matchInsideBrackets(l)
        print("[aa]", isNotValid)

        if isValid is True and isNotValid is False:
            list.append(isValid)

    return list

def matchOutsideBrackets(second):
    f = second.find("[")
    s = second.find("]")

    if f == -1:
        return isValid(second)

    firstHalf = second[:f]
    secondHalf = second[s + 1:]

    return isValid(firstHalf) | matchOutsideBrackets(secondHalf)

def matchInsideBrackets(second):
    f = second.find("[")
    s = second.find("]")

    if f == -1:
        return False
    
    inBrackets = second[f+1:s]
    secondHalf = second[s + 1:]

    return isValid(inBrackets) | matchInsideBrackets(secondHalf)


def isValid(s):
    print(s)
    for i in range(3, len(s)):
        if s[i-3] == s[i] and s[i-2] == s[i-1] and (s[i] != s[i-2]):
            return True
    
    return False


if __name__ == "__main__":
    validLines = partOne()
    filtered = [t for t in validLines if t is True ]
    count = len(filtered)
    print(count)