opDict = {"A": 0, "B": 1, "C": 2}
plDict = {"X": 0, "Y": 1, "Z": 2}


# (opponent - player + 1)%3 -> 1 if tie, 2 if won, 0 if lost
score1 = lambda opponent, player: (player + 1) + 3*((player - opponent + 1) % 3)

# (opponent + (choice - 1))%3 -> 0 if rock, 1 if paper, 2 if scissors
score2 = lambda opponent, choice: (1 + (opponent + choice - 1)%3) + 3*choice

with open("input.txt", "r") as file:
    inp = [line.strip().split() for line in file.readlines()]
    inp = [(opDict[a], plDict[b]) for (a,b) in inp]

part1 = sum([score1(a, b) for (a,b) in inp])

part2 = sum([score2(a,b) for (a,b) in inp])
