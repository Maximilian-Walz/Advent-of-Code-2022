def calcScore(x, y, grid):
    height = int(grid[x][y])
    
    # Top
    topScore = 0
    for i in range(x - 1, -1, -1):
        topScore += 1
        if int(grid[i][y]) >= height:
            break

    # Bottom
    bottomScore = 0
    for i in range(x + 1, len(grid)):
        bottomScore += 1
        if int(grid[i][y]) >= height:
            break

    # Left
    leftScore = 0
    for i in range(y - 1, -1, -1):
        leftScore += 1
        if int(grid[x][i]) >= height:
            break

    # Right
    rightScore = 0
    for i in range(y + 1, len(grid[0])):
        rightScore += 1
        if int(grid[x][i]) >= height:
            break
    
    return topScore * bottomScore * leftScore * rightScore


with open("input.txt") as file:
    grid = [list(line.strip()) for line in file.readlines()]

    topScore = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            score = calcScore(i, j, grid)
            if score > topScore:
                topScore = score

    print(topScore)