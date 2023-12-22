import sys


def mapper(seed, map):
    for i in map:
        s, d, r = [int(x) for x in i.split()]
        if d <= seed < d + r:
            return s + (seed - d)
    return seed


def readFile(file):
    with open(file, "r") as f:  # Potentially risky line (file opening)
        data = f.read()
        cat = data.split("\n\n")
        seeds = [int(x) for x in cat[0].split(":")[1].strip().split(" ")]
        maps = [val.split(":")[1].strip().split("\n") for val in cat[1:]]
        min = 999
        for j in range(len(seeds)):
            if j % 2 == 0 or j == 0:
                start = seeds[j]
                end = seeds[j + 1] + seeds[j]
                for i in range(start, end):
                    for map in maps:
                        i = mapper(i, map)
                    if i < min:
                        min = i
        print(min)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)
    readFile(sys.argv[1])
