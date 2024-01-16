import sys


def readFile(file):
    with open(file) as f:
        lines = f.read()
        seedsRange = [
            int(x) for x in lines.split("\n\n")[0].split(":")[1].strip().split(" ")
        ]
        allMaps = [
            [
                [int(j) for j in i.split(" ")]
                for i in x.split("\n")
                if i != x.split("\n")[0] and i != ""
            ]
            for x in lines.split("\n\n")
            if x != lines.split("\n\n")[0]
        ]
        seeds = [
            (x, x + seedsRange[i + 1])
            for i, x in enumerate(seedsRange)
            if i % 2 == 0 or i == 0
        ]
        for maps in allMaps:
            new = []
            while len(seeds) > 0:
                start, end = seeds.pop()
                for d, s, r in maps:
                    os = max(start, s)
                    oe = min(end, s + r)
                    if os < oe:
                        new.append((os - s + d, oe - s + d))
                        if os > start:
                            seeds.append((start, os))
                        if oe < end:
                            seeds.append((oe, end))
                        break
                else:
                    new.append((start, end))
            seeds = new
        print(min(seeds)[0])


if __name__ == "__main__":
    readFile(sys.argv[1])
    exit(0)
