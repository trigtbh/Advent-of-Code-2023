import aoc
contents = aoc.get_input(2023, 4).strip()
del aoc

# ---

class Card:
    def __init__(self, n, winning, have):
        self.n = n
        self.w = winning
        self.h = have

cards = {}
total = []

c = 0
for line in contents.split("\n"):
    _, a = line.split(": ")
    winning, have = a.split(" | ")
    w = [int(x) for x in winning.split(" ") if x]
    h = [int(x) for x in have.split(" ") if x]
    n = int(_.split(" ")[-1])
    cards[n] = (Card(n, w, h))

to_add = list(cards.keys())

mapped = {n: 1 for n in to_add}

for item in to_add:
    c = cards[item]
    match_ = 0
    for i in c.w:
        if i in c.h:
            match_ += 1
    for x in range(match_):
        mapped[c.n + x + 1] += mapped[item]
    
print(sum(list(mapped.values())))