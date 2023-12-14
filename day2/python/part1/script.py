import re
import sys


def determinePossibleGames(text):
    configuration = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    correct = 1
    sets = text.split(";")
    for set in sets:
        game = {}
        matches = re.findall("[0-9]+ [a-zA-Z]+", set)
        for match in matches:
            colorCube = match.split(" ")
            if colorCube[1] in game:
                game[colorCube[1]] += int(colorCube[0])
            else:
                game[colorCube[1]] = int(colorCube[0])
            if "blue" in game:
                if configuration["blue"] < game["blue"]:
                    correct = 0
            if "red" in game:
                if configuration["red"] < game["red"]:
                    correct = 0
            if "green" in game:
                if configuration["green"] < game["green"]:
                    correct = 0
    if correct == 1:
        matched = re.search("[0-9]+:", text)
        if matched:
            return matched.group()[:-1]
    else:
        return 0


def sumOfIds(arr):
    sum = 0
    for item in arr:
        sum += int(item)
    return sum


def readFile(file):
    possibleGames = []
    with open(file, "r") as f:
        for line in f:
            game = determinePossibleGames(line)
            if game != 0:
                possibleGames.append(game)
    return sumOfIds(possibleGames)


if __name__ == "__main__":
    answer = readFile(sys.argv[1])
    print(answer)
