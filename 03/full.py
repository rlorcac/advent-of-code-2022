# this is a very stupid and inefficient way to calculate this
# DON'T DO THIS

def calculate1(string):
    first = set(string[0:len(string)//2])
    second = set(string[len(string)//2:])
    # print(out)
    out = "".join(list(first.intersection(second)))
    out = priority(out)
    return out

def calculate2(a,b,c):
    a = set(a.strip())
    b = set(b.strip())
    c = set(c.strip())
    out = a.intersection(b)
    out = out.intersection(c)
    # print(out)
    out = "".join(list(out))
    out = priority(out)
    return out

def priority(ch):
    out = ord(ch) - 96
    out = out%64
    out -= 6*int(out > 26)
    return out

with open("input.txt", "r") as file:
    inp = file.readlines()

part1 = sum([calculate1(s.strip()) for s in inp])

part2 = 0
for i in range(len(inp)//3):
    (a,b,c) = inp[3*i:3*i+3]
    part2 += calculate2(a,b,c)
    
print(part1)

print(part2)
