import sys


def readFile(file):
    with open(file, "r") as f:
        points = 0
        for line in f:
            winningCards = [
                x
                for x in line.split(":")[1].split("|")[0].strip().split(" ")
                if x != ""
            ]
            cards = [
                x
                for x in line.split(":")[1].split("|")[1].strip().split(" ")
                if x != ""
            ]
            count = 0
            for card in cards:
                if card in winningCards:
                    count += 1
            if count > 0:
                points += 2 ** (count - 1)
    print(points)


if __name__ == "__main__":
    readFile(sys.argv[1])
