import sys


def readFile(file):
    with open(file, "r") as f:
        sum = 0
        cs = set()
        data = f.read()
        lines = data.strip().split("\n")
        for r in range(len(lines)):
            for c in range(len(lines)):
                arr = set()
                if lines[r][c] != "*":
                    continue
                for cr in [r - 1, r, r + 1]:
                    for cc in [c - 1, c, c + 1]:
                        if (
                            cr < 0
                            or cr >= len(lines)
                            or cc < 0
                            or cc >= len(lines[cr])
                            or not lines[cr][cc].isdigit()
                        ):
                            continue
                        while cc > 0 and lines[cr][cc - 1].isdigit():
                            cc -= 1
                        arr.add((cr, cc))
                if len(arr) != 2:
                    continue
                num = []
                for cr, cc in arr:
                    string = ""
                    while cc < len(lines[cr]) and lines[cr][cc].isdigit():
                        string += lines[cr][cc]
                        cc += 1
                    num.append(int(string))
                sum += num[0] * num[1]
        print(sum)


if __name__ == "__main__":
    readFile(sys.argv[1])
