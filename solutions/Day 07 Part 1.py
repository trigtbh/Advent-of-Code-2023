import aoc
contents = aoc.get_input(2023, 7).strip()
del aoc

# ---

chars = "AKQJT98765432"
assert len(chars) == 13

def sort(s):
    i = len(s) - 1
    at = s[i]
    atvals = [chars.index(c) for c in at[0]]
    while i > 0:
        at = s[i]
        compvals = [chars.index(c) for c in s[i - 1][0]]
        through = False
        for n in range(len(atvals)):
            if atvals[n] > compvals[n]:
                s[i], s[i - 1] = s[i - 1], s[i]
                through = True
                break
            elif atvals[n] < compvals[n]: break
        i -= 1
        if not through: break


fivekind = []
fourkind = []
fullhouse = []
threekind = []
twopair = []
onepair = []
high = []

s = []
for line in contents.split("\n"):
    cards, bid = line.split(" ")
    
    counter = {
        l: cards.count(l) for l in set(cards)
    }

    vs = list(counter.values())
    if vs[0] == 5:
        fivekind.append((cards, bid, 7)) # FL
        sort(fivekind)
        continue

    if any(x == 4 for x in vs):
        fourkind.append((cards, bid, 6)) # FL
        sort(fourkind)
        continue

    if len(vs) == 2:
        fullhouse.append((cards, bid, 5)) # FL
        sort(fullhouse)
        continue

    if any(x == 3 for x in vs):
        threekind.append((cards, bid, 4)) # FL
        sort(threekind)
        continue

    if vs.count(2) == 2:
        twopair.append((cards, bid, 3))
        sort(twopair)
        continue

    elif vs.count(2) == 1:
        onepair.append((cards, bid, 2))
        sort(onepair)
        continue

    else:
        high.append((cards, bid, 1))
        sort(high)

x = 0

for i, b in enumerate(high + onepair + twopair + threekind + fullhouse + fourkind + fivekind):
    x += int(b[1]) * (i + 1)

print(x)