with open("input.txt", "r") as file:
    inp = file.read().split("\n\n")
    inp = [[int(elem) for elem in elf.strip().split("\n")] for elf in inp]


sums = [sum(elf) for elf in inp]
sums.sort()

part1 = sums[-1]
part2 = sum(sums[-3:])

print(part1)
print(part2)
