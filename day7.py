from collections import defaultdict

data = open("input_day7.txt").read().strip().split("\n")
sizes = defaultdict(int)
#print(sizes)
path = []
#counter = 0
for line in data:
    if line.startswith("$ cd"):
        d = line.split()[2]
        if d == "/":
            path.append("/")
        elif d == "..":
            last = path.pop()
        else:
            path.append(f"{path[-1]}{'/' if path[-1] != '/' else ''}{d}")
            # print(path)
            # counter += 1
            # if counter == 5:
            #     break
    
    if line[0].isnumeric():
        for p in path:
            sizes[p] += int(line.split()[0])

print(f"Part 1: {sum(s for s in sizes.values() if s <= 100_000)}")
print(f"Part 2: {min(s for s in sizes.values() if s >= 30_000_000 - (70_000_000 - sizes['/']))}")