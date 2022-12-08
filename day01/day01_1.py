with open("input.txt") as file:
    sums = sorted([sum([int(elve) for elve in elve.split("\n")]) for elve in file.read().split("\n\n")])
    print(sums[-1])