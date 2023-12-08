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
# for p in n:
#     pointers.append([p, 0])

pointers.append(["AAA", 0])

i = 0
while True:
    instruction = inst[i]
    for x in range(len(pointers)):
        pointer = pointers[x]
        if pointer[0] == "ZZZ":
            print(pointer[1])
            exit()
        l, r = n[pointer[0]]
        if instruction == "L":
            pointer[0] = l
        else:
            pointer[0] = r
        pointer[1] += 1
    i = (i + 1) % len(inst)