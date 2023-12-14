import re
import sys


def determineMinCubes(text):
    answer = 1
    game = {}
    matches = re.findall("[0-9]+ [a-zA-Z]+", text)
    for match in matches:
        colorCube = match.split(" ")
        if colorCube[1] in game:
            if game[colorCube[1]] < int(colorCube[0]):
                game[colorCube[1]] = int(colorCube[0])
        else:
            game[colorCube[1]] = int(colorCube[0])
    for cube in game:
        answer *= game[cube]
    return answer


def readFile(file):
    sum = 0
    with open(file, "r") as f:
        for line in f:
            sum += determineMinCubes(line)
    return sum


if __name__ == "__main__":
    answer = readFile(sys.argv[1])
    print(answer)
