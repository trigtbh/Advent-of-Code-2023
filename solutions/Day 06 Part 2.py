import aoc
contents = aoc.get_input(2023, 6).strip()
del aoc

# ---

times, distances = contents.split("\n")
t = int(times.split(": ")[1].replace(" ", ""))
d = int(distances.split(": ")[1].replace(" ", ""))

c = 0
for n in range(t):
    if n * (t - n) > d:
        c += 1

print(c)