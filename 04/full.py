sign = lambda x: -1 if x < 0 else (1 if x > 0 else 0)

def p1(i):
    ctr = 0
    for ((a1, b1), (a2, b2)) in i:
        ctr += int(abs(sign(a1-a2)+sign(b1-b2)) <= 1)
    return ctr

def p2(i):
    ctr = 0
    for ((a1, b1), (a2, b2)) in i:
        ctr += int((a1 <= b2 and b1 >= b2) or (a2 <= b1 and b2 >= b1))
    return ctr

with open("input.txt","r") as file:
    inp = [[[int(x) for x in thing.split("-")] for thing in line.strip().split(",")] for line in file.readlines()]


part1 = p1(inp)
part2 = p2(inp)
