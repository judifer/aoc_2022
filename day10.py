inp = [x.strip() for x in open("day10.txt").readlines()]

x = 1
cnt = 0
vals = [20, 60, 100, 140, 180, 220]
imp = 0
grid = [[" "] * 40 for _ in range(6)]
draw = 0

for line in inp:
    if line == "noop":
        if abs(x - cnt % 40) <= 1:
                grid[draw][cnt % 40] = "#"
        cnt += 1
        if cnt in vals:
            imp += cnt * x
        if cnt % 40 == 0:
            draw += 1
    else:
        _, a = line.split()
        for i in range(2):
            if abs(x - cnt % 40) <= 1:
                grid[draw][cnt % 40] = "#"
            cnt += 1
            if cnt in vals:
                imp += cnt * x
            if cnt % 40 == 0:
                draw += 1
        x += int(a)

print("Part one:", imp)
for i in grid:
    print("".join(i))