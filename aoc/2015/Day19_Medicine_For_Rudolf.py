from itertools import permutations
from itertools import pairwise

molicules = set()
listTrans = []
transformations = """H => HO
H => OH
O => HH"""

starting = "HOH"

def parse():
    global transformations
    t = transformations.split("\n")
    global listTrans
    listTrans = list(t)

def main(tranNum):
    sb = ""
    global molicules
    global starting

    for i in starting:
        lookup = listTrans[tranNum]
        s, t = lookup.split(" => ")
        if i == s:
            newMol = starting[:i] + t + starting[i+1:]
            molicules.add(newMol)
        print(sb)
            
    

if __name__ == "__main__":
    parse()

    for i in range(len(listTrans)):
        main(i)