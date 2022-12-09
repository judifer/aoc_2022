dirs = [x.strip().split() for x in open("day09.txt").readlines()]
dx, dy = {"R": 1, "L": -1, "U": 0, "D": 0}, {"R": 0, "L": 0, "U": -1, "D": 1}
h, t = (0, 0), [(0, 0) for i in range(9)]

def tails(h, t):
    diffy, diffx = (h[0] - t[0]), (h[1] - t[1])
    if abs(diffy) < 2 and abs(diffx) < 2:
        pass
    elif abs(diffy) > 1 and abs(diffx) > 1:
        t = (h[0] - 1 if t[0] < h[0] else h[0] + 1, h[1] - 1 if t[1] < h[1] else h[1] + 1)
    elif abs(diffy) > 1:
        t = (h[0] - 1 if t[0] < h[0] else h[0] + 1, h[1])
    elif abs(diffx) > 1:
        t = (h[0], h[1] - 1 if t[1] < h[1] else h[1] + 1)
    return t

visited = set([t[0]])
visited_end = set([t[8]])

for dir in dirs:
    go, dis = dir[0], int(dir[1])
    for i in range(dis):
        h = (h[0] + dy[go], h[1] + dx[go])
        t[0] = tails(h, t[0])
        for j in range(1, 9):
            t[j] = tails(t[j -1], t[j])
        visited_end.add(t[8])
        visited.add(t[0])

print(f"Part one: {len(visited)} | Part two: {len(visited_end)}")