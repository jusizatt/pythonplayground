import sys
import random
from math import isnan

class Hogwarts:
    @staticmethod
    def houses():
        return ["Gryfindor", "Hufflepuff", "RavenClaw", "Slytherin"]

def select_house():
    house = random.choice(Hogwarts.houses())
    return house

def select_house_by_num(num):
    return Hogwarts.houses()[num]

# if __name__ == "__main__":
#     import sys
#     if len(sys.argv) > 1:
#         number = int(sys.argv[1])
#         if not isnan(number):
#             print(f"You belong to {select_house_by_num(number)}!")
#     else:
#         print(f"You belong to {select_house()}!")