import sys


def readFile(file):
    with open(file, "r") as f:  # Potentially risky line (file opening)
        data = f.read()
        cat = data.split("\n\n")
        seedline = [int(x) for x in cat[0].split(":")[1].strip().split(" ")]
        maps = [val.split(":")[1].strip().split("\n") for val in cat[1:]]
        seeds = []
        for j in range(0, len(seedline), 2):
            seeds.append((seedline[j], seedline[j] + seedline[j + 1]))
        for map in maps:
            ranges = []
            for i in map:
                d, s, r = [int(x) for x in i.split(" ")]
                ranges.append((d, s, r))
            new = []
            while len(seeds) > 0:
                start, end = seeds.pop()
                for d, s, r in ranges:
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
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)
    readFile(sys.argv[1])
