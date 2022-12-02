inp = sorted(sum(int(y) for y in x.split("\n")) for x in open("day01.txt").read().split("\n\n"))
print("Part one:", inp[-1], "| Part two:", sum(inp[-3:]))