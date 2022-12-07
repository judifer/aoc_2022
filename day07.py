# split the input into lines, and each line at " "
inp = [x.strip().split() for x in open("day07.txt").readlines()]
# dictionaries for the sums of each individual dir and the immediate path available from each dir
path = dict()
sums = dict()

for idx, line in enumerate(inp):
    if line[1] == "cd":     # check for start of directory contents
        if line[2] == "..":     # ignore those moving back to previous folder as new step
            continue
        else:
            path[line[2]] = []      # add dir to path
            sums[line[2]] = 0       # add dir to sums
            for i in range(1, len(inp) - idx):      # check the lines following our original dir
                content = inp[idx + i]
                if content[1] == "cd":          # finish checking contents when it moves out of dir
                    break
                elif content[0] == "dir":       # add included dirs to path for original dir
                    path[line[2]].append(content[1])
                elif content[1] == "ls":        # ignore ls
                    continue
                else:
                    sums[line[2]] += int(content[0])        # add value of just this dir to sums

total_size = dict()
for i in sums:          # initiate each dir in dict
    total_size[i] = 0

def searcher(i, path, sums, cnt):   # go through every path and sum all the dirs inside it
    if len(path[i]) > 0:
        for j in path[i]:
            cnt += searcher(j, path, sums, cnt)     
    cnt += sums[i]
    return cnt


for i in path:          # initiate searcher function for each dir
    cnt = 0
    total_size[i] += searcher(i, path, sums, cnt)

result = 0
for i in total_size:                # sum all dirs smaller than 100000
    if total_size[i] <= 100000:
        result += total_size[i]

print(result)