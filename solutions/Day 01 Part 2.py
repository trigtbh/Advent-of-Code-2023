import aoc
contents = aoc.get_input(2023, 1)
del aoc

# ---
f = 0
for line in contents.split("\n"):
    
    items = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "1", "2", "3", "4", "5", "6", "7", "9", "8"]
    
    for x in range(9):
        for y in range(9):
            if items[x][-1] == items[y][0]:
                line = line.replace(items[x][:-1] + items[y], items[x] + items[y])
    
    
    n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        line = line.replace(items[i], str(n[i]))



    
    chars = "".join([c for c in line if c in "1234567890"])
    # print(chars[0], chars[-1])
    # input()

    f += int(chars[0] + chars[-1])

print(f)