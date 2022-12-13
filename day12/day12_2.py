def pprintMap(map):
    for line in map:
        for tile in line:
            if tile == -1:
                print(".", end="")
            else: 
                print("#", end="")
        print()
    print()


def printMap(map):
    for line in map:
        for tile in line:
            print(tile, end="")
        print()
    print()


with open("input.txt") as file:
    # Read map and find start and end
    map = []
    for i, line in enumerate(file.readlines()):
        mapLine = []
        for j, tile in enumerate(line.strip()):
            if tile == "S":
                end = (i,j)
                mapLine.append('a')
            elif tile == "E":
                start = (i,j)
                mapLine.append('z')
            else:
                mapLine.append(tile)
        map.append(mapLine)

    distanceMap = [[0 if j == start[0] and i == start[1] else -1 for i in range(len(map[0]))] for j in range(len(map))]

    # BFS to find shortest path
    current = start
    toVisit = [start]
    steps = 0

    while map[current[0]][current[1]] != 'a':
        # Find next node to visit
        current = toVisit.pop(0)
        steps = distanceMap[current[0]][current[1]] + 1

        # Add new nodes to visit
        for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if current[0] + x < 0 or current[0] + x >= len(map) or current[1] + y < 0 or current[1] + y >= len(map[0]):
                continue
            tile = map[current[0] + x][current[1] + y]
            distanceTile = distanceMap[current[0] + x][current[1] + y]
            if distanceTile != -1:
                continue
            elif ord(tile) - ord(map[current[0]][current[1]]) >= -1:
                toVisit.append((current[0] + x, current[1] + y))
                distanceMap[current[0] + x][current[1] + y] = steps
        pprintMap(distanceMap)

    print(distanceMap[current[0]][current[1]])


