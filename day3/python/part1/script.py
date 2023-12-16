import sys


def readFile(file):
    cs = set()
    with open(file, "r") as f:
        data = f.read()
        lines = data.strip().split("\n")
        for r in range(len(lines)):
            for c in range(len(lines[r])):
                if lines[r][c].isdigit() or lines[r][c] == ".":
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
                        cs.add((cr, cc))
    nums = []
    for r, c in cs:
        string = ""
        while c < len(lines[r]) and lines[r][c].isdigit():
            string += lines[r][c]
            c += 1
        nums.append(int(string))
    print(sum(nums))


if __name__ == "__main__":
    readFile(sys.argv[1])
