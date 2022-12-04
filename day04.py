sections = [[y.split("-") for y in x.strip().split(",")] for x in open("day04.txt").readlines()]
cnt_1, cnt_2 = 0, 0

for section in sections:
    first, second, third, fourth = int(section[0][0]), int(section[0][1]), int(section[1][0]), int(section[1][1])
    a = set(range(first, second + 1))
    b = set(range(third, fourth + 1))
    if a.issubset(b) or b.issubset(a):
        cnt_1 += 1
    if len(a.intersection(b)) > 0:
        cnt_2 += 1

print(f"Part one: {cnt_1} | Part two: {cnt_2}")