import aoc
contents = aoc.get_input(2023, 7).strip()
del aoc

# ---

chars = "AKQT98765432J"
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
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    l5 = []
    l6 = []
    l7 = []
    for x in range(len(chars) - 1):
        fakec = cards.replace("J", chars[x])
        counter = {
            l: fakec.count(l) for l in set(fakec)
        }

        vs = list(counter.values())
        if vs[0] == 5:
            l7.append((cards, bid, 7)) # FL
            sort(l7)
            continue

        if any(x == 4 for x in vs):
            l6.append((cards, bid, 6)) # FL
            sort(l6)
            continue

        if len(vs) == 2:
            l5.append((cards, bid, 5)) # FL
            sort(l5)
            continue

        if any(x == 3 for x in vs):
            l4.append((cards, bid, 4)) # FL
            sort(l4)
            continue

        if vs.count(2) == 2:
            l3.append((cards, bid, 3))
            sort(l3)
            continue

        elif vs.count(2) == 1:
            l2.append((cards, bid, 2))
            sort(l2)
            continue

        else:
            l1.append((cards, bid, 1))
            sort(l1)


    
    highest = (l1 + l2 + l3 + l4 + l5 + l6 + l7)[-1]
    for i, tl in enumerate([l1, l2, l3, l4, l5, l6, l7]):
        if len(tl) > 0 and highest == tl[-1]:
            [high, onepair, twopair, threekind, fullhouse, fourkind, fivekind][i].append(highest)
            sort([high, onepair, twopair, threekind, fullhouse, fourkind, fivekind][i])
            break

x = 0

for i, b in enumerate(high + onepair + twopair + threekind + fullhouse + fourkind + fivekind):
    x += int(b[1]) * (i + 1)

print(x)