import sys
import re


def extractNumbers(text):
    matches = re.findall("\d", text)
    return int(str(matches[0]) + str(matches[-1]))


def readFile(file):
    totalSum = 0
    with open(file, "r") as f:
        for line in f:
            num = extractNumbers(line)
            totalSum += num
    return totalSum


if __name__ == "__main__":
    filePath = sys.argv[1]
    answer = readFile(filePath)
    print(answer)
