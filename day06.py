inp = open("day06.txt").read()

for idx, signal in enumerate(inp):
    marker = set()
    message = set()
    for i in range(4):
        marker.add(inp[idx + i])
    if len(marker) == 4:
        break

for idx_2, signal in enumerate(inp):
    marker = set()
    for i in range(14):
        marker.add(inp[idx_2 + i])
    if len(marker) == 14:
        break

print(f"Part one: {idx + 4} | Part two: {idx_2 + 14}")