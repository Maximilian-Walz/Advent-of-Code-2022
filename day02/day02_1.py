with open("input.txt") as file:
    score = 0
    for line in file.read().splitlines():
        opponent = ord(line[0]) - 64
        me = ord(line[2]) - 23 - 64

        score += me
        if me == opponent:
            score += 3
        if (opponent == 1 and me == 2) or (opponent == 2 and me == 3) or (opponent == 3 and me == 1):
            score += 6

    print(score)
        
        
        