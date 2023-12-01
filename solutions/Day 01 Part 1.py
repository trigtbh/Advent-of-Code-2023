import aoc
contents = aoc.get_input(2023, 1).strip()
del aoc

# ---

c = 0
for line in contents.split("\n"):
    chars = "".join([c for c in line if c in "1234567890"])
    c += int(chars[0] + chars[-1])

print(c)