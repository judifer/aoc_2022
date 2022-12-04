sections = [x.strip().split(",") for x in open("day04.txt").readlines()]
cnt_1 = 0
cnt_2 = 0

for section in sections:
    first, second= section[0].split("-")
    third, fourth = section[1].split("-")
    first, second, third, fourth = int(first), int(second), int(third), int(fourth)
    if first == second:
        a = set()
        a.add(first)
    else:
        a = set(range(first, second + 1))
    if third == fourth:
        b = set()
        b.add(third)
    else:
        b = set(range(third, fourth + 1))
    if a.issubset(b) or b.issubset(a):
        cnt_1 += 1
    if len(a.intersection(b)) > 0:
        cnt_2 += 1

print(f"Part one: {cnt_1} | Part two: {cnt_2}")