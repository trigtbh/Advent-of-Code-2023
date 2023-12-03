import aoc
contents = aoc.get_input(2023, 3).strip()
del aoc

# ---

c = 0

added = set()

class Gear:
    def __init__(self, y, x):
        self.y = y
        self.x = x
        self.ns = []

gears = {}

lines = contents.split("\n")
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if (y, x) in added: continue
        char = lines[y][x]
        if char in "0123456789":
            sset = set()
            pl = x
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    if 0 <= y + dy < len(lines) and 0 <= x + dx < len(lines[0]):
                        sset.add((y + dy, x + dx))
            sset.discard((y, x))
            added.add((y, x))
            pr = x
            while pr < len(lines[0]) - 1 and lines[y][pr + 1] in "1234567890":
                pr += 1
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if 0 <= y + dy < len(lines) and 0 <= pr + dx < len(lines[0]):
                            sset.add((y + dy, pr + dx))
                sset.discard((y, pr))
                added.add((y, pr))
            # print(sorted(sset))
            # input()
            for item in sset:
                cy, cx = item
                if lines[cy][cx] not in "1234567890.":
                    if (cy, cx) in gears:
                        gears[(cy, cx)].ns.append(int(lines[y][pl:pr + 1]))
                    else:
                        if lines[cy][cx] == "*":
                            gears[(cy, cx)] = Gear(y, x)
                            gears[(cy, cx)].ns.append(int(lines[y][pl:pr + 1]))


c = 0
for gear in gears:
    g = gears[gear]
    if len(g.ns) == 2:
        c += g.ns[0] * g.ns[1]
print(c)