sacks = [x.strip() for x in open("day03.txt").readlines()]

cnt = 0

for sack in sacks:
    first = set(sack[:(len(sack) // 2)])
    second = set(sack[(len(sack) // 2):])
    letter = list(first.intersection(second))[0]
    if letter.islower():
        cnt += ord(letter) - 96
    else:
        cnt += ord(letter) - 38

print("Part 1:", cnt)

jmp = 0
cnt = 0
while jmp <= (len(sacks) - 1):
    a = set(sacks[jmp])
    b = set(sacks[jmp + 1])
    c = set(sacks[jmp + 2])
    letter = list(a.intersection(b, c))[0]
    if letter.islower():
        cnt += ord(letter) - 96
    else:
        cnt += ord(letter) - 38
    jmp += 3

print("Part two:", cnt)