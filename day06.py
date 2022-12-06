inp = open("day06.txt").read()

def finder(inp, nums):
    for idx, signal in enumerate(inp):
        marker = set()
        message = set()
        for i in range(nums):
            marker.add(inp[idx + i])
        if len(marker) == nums:
            return idx + nums

print(f"Part one: {finder(inp, 4)} | Part two: {finder(inp, 14)}")