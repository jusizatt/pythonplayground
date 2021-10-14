from re import split

class Tag:
    def __init__(self, line):
        if line.find(" -> ") == -1:
            tagParts = line.split(" (")
            self.tag = tagParts[0]
            self.weight = int(tagParts[1][:-1])
            self.branches = None
        else:
            (tagAndWeight, tagBranches) = line.split(" -> ")
            tagParts = tagAndWeight.split(" (")
            self.tag = tagParts[0]
            self.weight = int(tagParts[1][:-1])
            self.branches = tagBranches.split(", ")

        self.parent = None
  
    def addParent(self, parentTag):
        self.parent = parentTag

def parse():
    file = open("C:\\W\\python\\aoc\\2017\\input\\aoc2017_day7_input.txt", "r")
    #file = open("C:\\W\\python\\aoc\\2017\\input\\aoc2017_day7_input_test.txt", "r")
    lines = file.read()

    tags = {}

    for line in lines.split('\n'):
        tagObj = Tag(line)
        tags[tagObj.tag] = tagObj

    return tags

def lookup(allTags: dict, currentTag: Tag):
    if currentTag.branches == None:
       currentTag.addParent(currentTag)
       return

    for i in range(len(currentTag.branches)):
        childTag = allTags[currentTag.branches[i]]
        childTag.addParent(currentTag)
        lookup(allTags, childTag)

def partOne():
    tags = parse()
    for t in range(len(tags)):
        tagsList = list(tags.values())
        lookup(tags, tagsList[t])

    for k, v in tags.items():
        if v.parent == None:
            print("Root Tag ", k)
    
    return tags

def partTwo(tags):
    #getWeights(tags, tags["tknk"])
    getWeights(tags, tags["qibuqqg"])

def getWeights(allTags: dict, currentTag: Tag, nested = 1):
    if currentTag.branches == None:
        return currentTag.weight

    weights = { 0 }
    childCount = len(currentTag.branches)
    for i in range(childCount):
        childTag = allTags[currentTag.branches[i]]
        w = getWeights(allTags, childTag, nested + 1)
        print(nested*"+", childTag.tag, w)
        weights.add(w)

    if len(weights) != 2:
        print(f"{currentTag.tag} Out of balance!!! Tag weight {currentTag.weight}. Set Weights: {weights}")

    return (sum(weights) * childCount) + currentTag.weight


if __name__ == "__main__":
    tags = partOne()
    partTwo(tags)