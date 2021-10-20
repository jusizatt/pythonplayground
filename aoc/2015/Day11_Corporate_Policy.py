from itertools import permutations
from itertools import pairwise

currentPass = "vzbxkghz"
partTwoPass = "vzbxxyzz"

class Counter:
    def __init__(self, passw):
        self.passw = passw
        self.passc = []

        for c in passw:
            self.passc.append(ord(c))

        print("Starting Positions...")
        self.display()
    
    def increment(self, index = 7):
        cval = self.passc[index] = self.passc[index] + 1
        if cval == ord("i") or cval == ord("o") or cval == ord("l"):
            self.increment(index)

        if cval == ord("{"):
            self.passc[index] = ord('a')
            self.increment(index - 1)

    def getPassStr(self):
        p = ""
        for i in self.passc:
            p += chr(i)
        
        return p

    def display(self):
        print("Password:", self.getPassStr())
        #print("PassCode:", self.passc)

    def check(self):
        seq = False
        for i in range(5):
            if self.passc[i] + 1 == self.passc[i + 1] and self.passc[i + 1] + 1 == self.passc[i + 2]:
                seq = True
                print(self.getPassStr())
        
        if seq is False:
            return False

        count = 0
        for p in pairwise(self.passc):
            if p[0] == p[1]:
                count + 1
            
            if count == 2:
                print(self.getPassStr())
                return True
    
#vzbxxyzz Part 1
#vzcaabcc Part 2
if __name__ == "__main__":
    c = Counter("vzbzefgg")
    while True:
        c.increment()
        c.display()
        if c.check():
            break