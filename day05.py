with open("day05.txt") as f:
    f_piles, f_ins = f.read().split("\n\n")

f_piles = f_piles.splitlines()
f_piles = f_piles[:-1]
f_ins = f_ins.splitlines()

piles = [[] for i in range(0, len(f_piles) + 1)]

for i in range(-1, (-1 - len(f_piles)), -1):
    for ind, pkg in enumerate(f_piles[i][1::4]):
        if pkg != " ":
            piles[ind].append(pkg)

piles_two = [x.copy() for x in piles]

ins = []
for i in f_ins:
    _, many, _, fro, _, to = i.split()
    ins.append([int(many), int(fro), int(to)])

for i in ins:
    many, fro, to = i
    for j in range(0, many):
        piles[to - 1].append(piles[fro - 1][-1])
        piles[fro - 1].pop()

pkg_one = ""

for i in piles:
    pkg_one += i[-1]

for i in ins:
    many, fro, to = i
    for j in range(0, many):
        piles_two[to - 1].append(piles_two[fro - 1][0 - many + j])
    for j in range(0, many):
        piles_two[fro - 1].pop()

pkg_two = ""
for i in piles_two:
    pkg_two += i[-1]

print(f"Part one: {pkg_one} | Part two: {pkg_two}")