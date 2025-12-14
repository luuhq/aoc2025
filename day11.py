graph = {}

with open("inputs/day11.txt") as file:
    for line in file:
        line = line.strip()
        parts = line.split(" ")
        graph[parts[0][:-1]] = parts[1:]

mem = {}


def count_paths_p1(x):
    if x in mem:
        return mem[x]

    if x == "out":
        return 1

    mem[x] = sum([count_paths_p1(edge) for edge in graph[x]])
    return mem[x]


print(f"Part 1: {count_paths_p1('you')}")

mem = {}


def count_paths_p2(x, dac=False, fft=False):
    if (x, dac, fft) in mem:
        return mem[(x, dac, fft)]

    if x == "out":
        if dac and fft:
            return 1
        else:
            return 0

    paths = 0
    for edge in graph[x]:
        paths += count_paths_p2(edge, dac or edge == "dac", fft or edge == "fft")

    mem[(x, dac, fft)] = paths
    return paths


print(f"Part 2: {count_paths_p2('svr')}")
