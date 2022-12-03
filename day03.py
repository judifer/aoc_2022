sacks = [x.strip() for x in open("day03.txt").readlines()]

cnt = 0

for sack in sacks:
    first = set(sack[:(len(sack) // 2)])
    second = set(sack[(len(sack) // 2):])
    letter = list(first & second)[0]
    if letter.islower():
        cnt += ord(letter) - 96
    else:
        cnt += ord(letter) - 38

print("Part 1:", cnt)

cnt = 0
for i in range(0, len(sacks), 3):
    a, b, c = sacks[i:i + 3]
    letter = list(set(a) & set(b) & set(c))[0]
    if letter.islower():
        cnt += ord(letter) - 96
    else:
        cnt += ord(letter) - 38

print("Part two:", cnt)