table = [[3, 1, 2], [1, 2, 3], [2, 3, 1]]

with open("input.txt") as file:
    score = 0
    for line in file.read().splitlines():
        opponent = ord(line[0]) - 65
        me = ord(line[2]) - 23 - 65
        score += me * 3
        score += table[opponent][me]
    print(score)
        