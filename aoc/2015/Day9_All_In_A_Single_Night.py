from itertools import permutations
from itertools import pairwise


citys = set()
cityDistances = {} 


def parseLine():
    #f = open("C:\\W\\python\\aoc\\2015\input\\aoc2015_day9_input_test.txt", "r")
    f = open("C:\\W\\python\\aoc\\2015\input\\aoc2015_day9_input.txt", "r")
    lines = f.read()

    for l in lines.split('\n'):
        parts = l.split(' ')
        global citys
        cityone = parts[0]
        citytwo = parts[2]
        citys.add(cityone)
        citys.add(citytwo)

        global cityDistances
        cityDistances[parts[0]+parts[2]] = int(parts[4])

    return list(citys)

#not 247
#is 117
if __name__ == "__main__":
    citys = parseLine()
    print(citys)

    p = permutations(citys)
    
    distances = {}
    for x in list(p):
        distance = 0

        for pa in pairwise(x):
            dis = cityDistances.get(pa[0]+pa[1]) if cityDistances.get(pa[0]+pa[1]) != None else cityDistances.get(pa[1]+pa[0])
            distance += dis

        distances[x] = distance
    
    #print(distances)
    min = min(distances.values())
    max = max(distances.values())
    print("part 1", min)
    print("part 2", max)