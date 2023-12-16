import sys


def readFile(file):
    with open(file, "r") as f:
        total = 0
        data = f.read()
        lines = data.split("\n")
        print(lines)
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
            for match in range(count):
                f += f[match - 1]
            total += count
        print(total)


if __name__ == "__main__":
    readFile(sys.argv[1])
