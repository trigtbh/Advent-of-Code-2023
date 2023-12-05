import aoc
contents = aoc.get_input(2023, 5).strip()
del aoc

# ---
vals = contents.split("\n\n")
seeds = [int(x) for x in vals[0].split(": ")[1].split(" ")]

maps_total = {}

for map_ in vals[1:]:
    temp, maps = map_.split(":\n")
    start, end = temp.split("-to-")
    end = end.split(" ")[0]
    to_add = {}
    for item in maps.split("\n"):
        dest, src, rng = item.split(" ")
        to_add[(int(src), int(src) + int(rng) - 1)] = int(dest)
    maps_total[(start, end)] = to_add

vals = seeds
start = "seed"
while start != "location":
    for item in maps_total:
        if item[0] == start:
            break
    temp = []
    for n in vals:
        good = False
        for pair in maps_total[item]:
            if pair[0] <= n <= pair[1]:
                temp.append(n - pair[0] + maps_total[item][pair])
                good = True
                break
        if not good:
            temp.append(n)
    
    vals = temp
    start = item[1]

print(min(vals))