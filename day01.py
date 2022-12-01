with open("day01.txt") as f:
    inp = sorted(sum(int(y) for y in x.split("\n")) for x in f.read().split("\n\n"))
print("Part one:", inp[-1], "| Part two:", sum(inp[-3:]))