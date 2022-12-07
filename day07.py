inp = [x.strip().split() for x in open("day07.txt").readlines()]

path = dict()
sums = dict()

curr = []
cnt = 0
for line in inp:
    if line[1] == "cd":
        if line[2] == "..":
            curr.pop()
        else:
            curr.append(line[2])
            path["".join(curr)] = []
            sums["".join(curr)] = 0
            cnt = 0
    elif line[1] == "ls":
        continue
    elif line[0] == "dir":
        path["".join(curr)].append("".join(curr) + line[1])
    else:
        sums["".join(curr)] += int(line[0])

total_size = dict()
for i in path:
    total_size[i] = 0

def searcher(i):
    if len(path[i]) > 0:
        for j in path[i]:
            searcher(j)  
    cnt.append(sums[i])
    return cnt

for i in path:
    cnt = list()
    cnt = searcher(i)
    total_size[i] += sum(cnt)

result = 0
for i in total_size:
    if total_size[i] <= 100000:
        result += total_size[i]

used_space = sum(list(sums.values()))
disc_space = 70000000
unused_space = 30000000
del_val = disc_space

for i in total_size:
    if (used_space - total_size[i]) <= (disc_space - unused_space) and total_size[i] < del_val:
        del_val = total_size[i]

print(f"Part one: {result} | Part two: {del_val}")