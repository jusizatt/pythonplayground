class Tracker:
    def __init__(self):
        self.point = (0,0)
        self.path = []

    def up(self):
        self.point = (self.point[0], (self.point[1] + 1))
        self.path.append(self.point)

    def down(self):
        self.point = (self.point[0], (self.point[1] - 1))
        self.path.append(self.point)

    def left(self):
        self.point = (self.point[0] - 1, (self.point[1]))
        self.path.append(self.point)

    def right(self):
        self.point = (self.point[0] + 1, (self.point[1]))
        self.path.append(self.point)

    def go(self, charDir):
        if charDir == '<':
            self.left()
        elif charDir == '>':
            self.right()
        elif charDir == 'v':
            self.down()
        elif charDir == '^':
            self.up()

    def unique(self):
        return len(set(self.path))
    
    def unique2(santa, robosanta):
        santa.extend(robosanta)
        return len(set(santa))

def Part1():
    f = open("C:\\W\\pythonplayground\\aoc\\2015\\aoc2015_day3_input.txt", "r")
    lines = f.read()
    tracker = Tracker()
    for c in iter(lines):
        tracker.go(c)

    count = tracker.unique()
    print("Part 1", count)

def Part2():
    f = open("C:\\W\\pythonplayground\\aoc\\2015\\aoc2015_day3_input.txt", "r")
    lines = f.read()
    
    santaTracker = Tracker()
    for c in iter(lines[0::2]):
        santaTracker.go(c)
    
    roboSantaTracker = Tracker()
    for c in iter(lines[1::2]):
        roboSantaTracker.go(c)

    count = Tracker.unique2(santaTracker.path, roboSantaTracker.path) 
    print("Part 2", count)

if __name__ == "__main__":
    Part1()
    Part2()