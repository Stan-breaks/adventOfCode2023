import sys


def readFile(file):
    with open(file, "r") as f:
        data = f.read()
        cat = data.split("\n\n")
        seeds = []
        maps = []
        for i, val in enumerate(cat):
            if i == 0:
                seeds = [int(x) for x in val.split(":")[1].strip().split(" ")]
            else:
                maps.append(val.split(":")[1].strip().split("\n"))
        for j, seed in enumerate(seeds):
            for map in maps:
                for i in map:
                    s, d, r = [int(x) for x in i.split(" ")]
                    if seed < (d + r) and seed >= d:
                        seeds[j] = s + (seed - d)
                        break
                print(seeds)
            print(seeds)
        print(seeds)


if __name__ == "__main__":
    readFile(sys.argv[1])
