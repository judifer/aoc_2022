from collections import defaultdict

inp = [x.strip() for x in open("day10.txt").readlines()]

x = 1
cnt = 0
vals = [20, 60, 100, 140, 180, 220]
imp = 0
grid = [[" "] * 40 for _ in range(6)]
draw = 0

def drawing(x, c, d):
    if abs(x - c % 40) <= 1:
        grid[d][c % 40] = "#"

for line in inp:
    if line == "noop":
        drawing(x, cnt, draw)
        cnt += 1
        if cnt in vals:
            imp += cnt * x
        if cnt % 40 == 0:
            draw += 1
    else:
        _, a = line.split()
        for i in range(2):
            drawing(x, cnt, draw)
            cnt += 1
            if cnt in vals:
                imp += cnt * x
            if cnt % 40 == 0:
                draw += 1
        x += int(a)

letters = defaultdict()
letters["F"] = [
    "####",
    "#   ",
    "### ",
    "#   ",
    "#   ",
    "#   "
]

letters["J"] = [
    "  ##",
    "   #",
    "   #",
    "   #",
    "#  #",
    " ## "
]

letters["U"] = [
    "#  #",
    "#  #",
    "#  #",
    "#  #",
    "#  #",
    " ## "
]

letters["B"] = [
    "### ",
    "#  #",
    "### ",
    "#  #",
    "#  #",
    "### "
]

letters["L"] = [
    "#   ",
    "#   ",
    "#   ",
    "#   ",
    "#   ",
    "####"
]

letters["R"] = [
    "### ",
    "#  #",
    "#  #",
    "### ",
    "# # ",
    "#  #"
]

letters["Z"] = [
    "####",
    "   #",
    "  # ",
    " #  ",
    "#   ",
    "####"
]


x = 0
y = 0
result = ""
while x < (len(grid[0]) - 2):
    letter = []
    for i in grid:
        letter.append("".join(i[x:x + 4]))
    for j in letters.keys():
        if letter == letters[j]:
            result += j
    x += 5

print(f"Part one: {imp} | Part two: {result}")