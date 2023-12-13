import sys
import re
from word2number import w2n


def extractNumbers(text):
    matches = re.findall('\d+|zero|one|two|three|four|five|six|seven|eight|nine`', text)
    numbers = []
    for match in matches:
        try:
            number = w2n.word_to_num(match)
            numbers.append(number)
        except ValueError:
            if match.isdigit():
                numbers.append(int(match))
    return int(str(numbers[0])+str(numbers[-1]))


def readFile(file):
    totalSum = 0
    with open(file, 'r') as f:
        for line in f:
            num = extractNumbers(line)
            totalSum += num
    return totalSum


if __name__ == "__main__":
    filePath = sys.argv[1]
    answer = readFile(filePath)
    print(answer)
