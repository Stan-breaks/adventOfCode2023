import sys


def readFile(file):
    with open(file, "r") as f:
        data = f.read()
        lines = data.strip().split("\n")
        for line in lines:
            count = 0
            winCards = [
                x
                for x in line.split(":")[1].split("|")[0].strip().split(" ")
                if x != ""
            ]
            cards = [
                x
                for x in line.split(":")[1].split("|")[1].strip().split(" ")
                if x != ""
            ]
            for card in cards:
                if card in winCards:
                    count += 1
            cardArr = [x for x in line.split(":")[0].split(" ") if x != ""]
            cardNum = int(cardArr[1])
            for i in range(count):
                lines.append(lines[cardNum + i])
        print(len(lines))


if __name__ == "__main__":
    readFile(sys.argv[1])
