def pprint(grid):
    for row in grid:
        print(''.join(row))
    print()

with open("input.txt") as file:
    # Parse input
    segments = [[(int(coords.split(",")[1]), int(coords.split(",")[0])) for coords in path.split(" -> ")] for path in file.read().splitlines()]

    # Find the smallest x and y values
    min_x = 0
    min_y = min([min([coords[1] for coords in segment]) for segment in segments])

    # Find the largest x and y values
    max_x = max([max([coords[0] for coords in segment]) for segment in segments])
    max_y = max([max([coords[1] for coords in segment]) for segment in segments])

    # Create a grid of the size of the input
    grid = [["." for _ in range(max_y - min_y + 1)] for _ in range(max_x - min_x + 1)]

    # Fill the grid with the input
    source = (0, 500 - min_y)
    grid[source[0]][source[1]] = "+"
    for segment in segments:
        for i, fst in enumerate(segment[:-1]):
            snd = segment[i + 1]
            start= min(fst, snd)
            end = max(fst, snd)
            for x in range(start[0], end[0] + 1):
                grid[x - min_x][start[1] - min_y] = "#"
            for y in range(start[1], end[1] + 1):
                grid[end[0] - min_x][y - min_y] = "#"
    

    def moveSandTo(origin, offset):
        destination = (origin[0] + offset[0], origin[1] + offset[1])
        grid[destination[0]][destination[1]] = "o"
        grid[origin[0]][origin[1]] = "."
        return destination

    def getTile(pos, offset):
        if pos[0] + offset[0] < 0 or pos[1] + offset[1] < 0 or pos[0] + offset[0] >= len(grid) or pos[1] + offset[1] >= len(grid[0]):
            return " "
        return grid[pos[0] + offset[0]][pos[1] + offset[1]]

    # Simulate sand falling
    numResting = 0

    abyss = False
    while not abyss:
        grid[source[0]][source[1]] = "o"
        sandPos = source
        resting = False
        while not resting:
            below = getTile(sandPos, (1, 0))
            if below == ".":
                sandPos = moveSandTo(sandPos, (1, 0))
            elif below != ".":
                left = getTile(sandPos, (1, -1))
                right = getTile(sandPos, (1, 1))
                if left == " ":
                    abyss = True
                    break
                elif left == ".":
                    sandPos = moveSandTo(sandPos, (1, -1))
                elif right == " ":
                    abyss = True
                    break
                elif right == ".": 
                    sandPos = moveSandTo(sandPos, (1, 1))
                else:
                    resting = True
                    numResting += 1
    pprint(grid)
    print(numResting)
