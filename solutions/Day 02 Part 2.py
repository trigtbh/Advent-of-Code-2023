import aoc
contents = aoc.get_input(2023, 2).strip()
del aoc

# ---

c = []
for g in contents.split("\n"):
    _, stuff = g.split(": ")
    colors = {"red": 0, "green": 0, "blue": 0}
    for n in stuff.split("; "):
        for pair in n.split(", "):
            number, color = pair.split(" ")
            number = int(number)
            if colors[color] < number:
                colors[color] = number

    power = colors["red"] * colors["green"] * colors["blue"]
    c.append(power)


print(sum(sorted(c)))