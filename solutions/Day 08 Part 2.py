import aoc
contents = aoc.get_input(2023, 8).strip()
del aoc

# ---
inst, nodes = contents.split("\n\n")

n = {}
for line in nodes.split("\n"):
    id_, contents = line.split(" = ")
    n[id_] = contents[1:-1].split(", ")


pointers = []
for p in n:
    if p[-1] == "A":
        pointers.append([p, 0])

leng = (len(inst))
c = 1


temp = []
for pointer in pointers:
    i = 0
    prev = []
    while True:
        instruction = inst[i]
        if pointer[0][-1] == "Z":
            break
        prev.append(pointer[0])
        l, r = n[pointer[0]]
        if instruction == "L":
            pointer[0] = l
        else:
            pointer[0] = r
        pointer[1] += 1
        i = (i + 1) % len(inst)
    c *= len(prev)
    temp.append(len(prev))

ds = set()
for x in temp:
    for n in range(1, x):
        if x % n == 0:
            ds.add(n)
n = 1
for item in ds:
    n *= item

print(n)