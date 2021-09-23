import hashlib

puzzleInput = "iwrupvqb"

def mineAdventCoins(part, hashStartsWith):
    count = 0
    while True:
        nextValue = puzzleInput + str(count)
        result = hashlib.md5(nextValue.encode()).hexdigest()

        if result.startswith(hashStartsWith):
            break
        
        count += 1

    print(part, count)

if __name__ == "__main__":
    mineAdventCoins("Part 1", "00000")
    mineAdventCoins("Part 2", "000000")