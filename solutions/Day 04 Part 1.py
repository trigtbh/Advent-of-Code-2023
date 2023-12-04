import aoc
contents = aoc.get_input(2023, 4).strip()
del aoc

# ---

c = 0
for line in contents.split("\n"):
    _, a = line.split(": ")
    winning, have = a.split(" | ")
    w = [int(x) for x in winning.split(" ") if x]
    h = [int(x) for x in have.split(" ") if x]

    i = 0
    for x in w:
        if x in h:
            i += 1
    if i:
        n = (2 ** (i - 1))
        c += n


print(c)