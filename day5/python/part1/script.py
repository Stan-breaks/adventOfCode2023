import sys


def mapper(seed, map):
    for i in map:
        s, d, r = [int(x) for x in i.split()]
        if d <= seed < d + r:
            return s + (seed - d)
    return seed


def readFile(file):
    with open(file, "r") as f:
        data = f.read()
        cat = data.split("\n\n")
        seeds = []
        maps = []
        result = []
        for i, val in enumerate(cat):
            if i == 0:
                seeds = [int(x) for x in val.split(":")[1].strip().split(" ")]
            else:
                maps.append(val.split(":")[1].strip().split("\n"))
        for seed in seeds:
            for map in maps:
                seed = mapper(seed, map)
            result.append(seed)
        print(min(result))


if __name__ == "__main__":
    readFile(sys.argv[1])
