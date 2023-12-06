import aoc
contents = aoc.get_input(2023, 6).strip()
del aoc

# ---

times, distances = contents.split("\n")
times = [int(t) for t in times.split(": ")[1].split(" ") if t]
distances = [int(t) for t in distances.split(": ")[1].split(" ") if t]

b =1 
for i in range(len(times)):
    c = 0    
    t = times[i]
    d = distances[i]
    for n in range(t):
        if n * (t - n) > d:
            c += 1
    b *= c

print(b)