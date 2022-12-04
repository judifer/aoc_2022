sections = [x.strip().split(",") for x in open("day04.txt").readlines()]
cnt_1, cnt_2 = 0, 0

for section in sections:
    first, second = section[0].split("-")
    third, fourth = section[1].split("-")
    a = set(range(int(first), int(second) + 1))
    b = set(range(int(third), int(fourth) + 1))
    if a.issubset(b) or b.issubset(a):
        cnt_1 += 1
    if len(a.intersection(b)) > 0:
        cnt_2 += 1

print(f"Part one: {cnt_1} | Part two: {cnt_2}")