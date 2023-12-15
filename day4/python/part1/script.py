import sys


def readFile(file):
    with open(file, "r") as f:
        points = 0
        for line in f:
            winningCards = line.split(":")[1].split("|")[0].strip().split(" ")
            cards = line.split(":")[1].split("|")[1].strip().split(" ")
            count = 0
            for card in cards:
                if card in winningCards:
                    if count > 0:
                        count *= 2
                    else:
                        count += 1
            print(count)
            points += count
        print(points)


if __name__ == "__main__":
    readFile(sys.argv[1])
