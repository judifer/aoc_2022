f_piles, f_ins = [x.splitlines() for x in open("day05.txt").read().split("\n\n")]

ins = []
for i in f_ins:
    _, many, _, fro, _, to = i.split()
    ins.append([int(many), int(fro), int(to)])

piles = [[] for i in range(0, len(f_piles))]
for i in range(-1, (-1 - len(f_piles)), -1):
    for ind, pkg in enumerate(f_piles[i][1::4]):
        if pkg != " ":
            piles[ind].append(pkg)
piles_two = [x.copy() for x in piles]

for i in ins:
    many, fro, to = i
    for j in range(0, many):
        piles[to - 1].append(piles[fro - 1][-1])
        piles[fro - 1].pop()
        piles_two[to - 1].append(piles_two[fro - 1][j - many])
        piles_two[fro - 1].pop(j - many)

pkg_one, pkg_two = "", ""
print(f"Part one: {pkg_one.join(i[-1] for i in piles)} | Part two: {pkg_two.join(i[-1] for i in piles_two)}")