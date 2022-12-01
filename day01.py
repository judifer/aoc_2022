with open("day01.txt") as f:
    inp = [x for x in f.read().split("\n\n")]

cals = list()

for i in inp:
    cnt = 0
    sing = [int(x) for x in i.split("\n")]
    for j in sing:
        cnt += j
    cals.append(cnt)

cals.sort()

print("Part one:", cals[-1])
print("Part two:", sum(cals[-3:]))
