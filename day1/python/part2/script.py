import sys


def extractNumbers(text):
    wordNums = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    numbers = []
    for i, c in enumerate(text):
        if c.isdigit():
            numbers.append(c)
        for d, val in enumerate(wordNums):
            if text[i:].startswith(val):
                numbers.append(d + 1)
    if numbers:
        return int(str(numbers[0]) + str(numbers[-1]))
    return 0


def readFile(file):
    totalSum = 0
    with open(file, "r") as f:
        for line in f:
            num = extractNumbers(line)
            if num:
                totalSum += num
    return totalSum


if __name__ == "__main__":
    filePath = sys.argv[1]
    answer = readFile(filePath)
    print(answer)
