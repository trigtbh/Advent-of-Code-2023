import aoc
contents = aoc.get_input(2023, 2).strip()
del aoc

# ---

c = 0

for g in contents.split("\n"):
    _, stuff = g.split(": ")
    possible = True
    for n in stuff.split("; "):
        for pair in n.split(", "):
            number, color = pair.split(" ")
            number = int(number)
            if (color == "blue" and number > 14) or (color == "red" and number > 12) or (color == "green" and number > 13):
                possible = False
                break
        if not possible:
            break
    if possible:
        c = c + int(_.split(" ")[1])
print(c)