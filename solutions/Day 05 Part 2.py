import aoc
contents = aoc.get_input(2023, 5).strip()
del aoc

# ---
vals = contents.split("\n\n")
seeds = [int(x) for x in vals[0].split(": ")[1].split(" ")]

sp = []
for i in range(len(seeds) // 2):
    sp.append([seeds[0], seeds[0] + seeds[1]])
    seeds = seeds[2:]

seeds = sp

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
    temp2 = []
    for range_ in vals:
        left, right = range_
        # for start, end in sorted(maps_total[item]):
        #     if left <= start <= end <= right:
        #         temp2.append([start, end])
        #         print(1)
        #     elif left <= start <= right <= end:
        #         temp2.append([start, right])
        #         print(2)
        #     elif start <= left <= end <= right:
        #         temp2.append([left, end])
        #         print(3)
        #     elif start <= left <= right <= end:
        #         temp2.append([left, right])
        #         print("B")

        # range splitting - from hell!
        c = [left, right]
        for start, end in sorted(maps_total[item]):
            if left <= start <= right:
                c.append(start)
            if left <= end <= right:
                c.append(end)
        c = (sorted(set(c)))



        for i in range(len(c) - 1):
            temp2.append([
                c[i], c[i+1]
            ])
    
    for range_ in temp2:
        left, right = range_
        good = False
        for start, end in maps_total[item]:
            if start <= left <= right <= end:
                temp.append([
                    left - start + maps_total[item][(start, end)],
                    right - start + maps_total[item][(start, end)]
                ])
                good = True
                break
        if not good:
            temp.append([left, right])
    vals = temp
    start = item[1]
print(min([v[0] for v in vals]))