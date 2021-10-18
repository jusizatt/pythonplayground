from typing import Set

citys = set() 


def parseLine():
    f = open("C:\\W\\pythonplayground\\aoc\\2015\input\\aoc2015_day9_input.txt", "r")
    lines = f.read()

    for l in lines.split('\n'):
        parts = l.split(' ')
        global citys
        citys.add(parts[0])
        citys.add(parts[2])

    return list(citys)

def tracePath(citys, currentPath = None):
    if currentPath == None:
        currentPath = []

    if len(citys) == 0:
        return currentPath

    path = []
    for eachPath in citys:
        currentPath.append(citys[0])
        return tracePath(citys[1:], currentPath)


if __name__ == "__main__":
    citys = parseLine()
    print(citys)
    paths = []
    for p in citys:
        path = tracePath(citys)
        paths.append(path)
        c = citys.pop(0)
        citys.append(c)
    
    print(paths)