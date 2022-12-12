def addX(tuple, value):
    return (tuple[0] + value, tuple[1])

def addY(tuple, value):
    return (tuple[0], tuple[1] + value)

with open("input.txt") as file:
    rope = []
    for i in range(10):
        rope.append((0, 0))

    visited_positions = [rope[9]]

    for line in file.readlines():
        direction = line.split(" ")[0]
        distance = int(line.split(" ")[1])


        for i in range(distance):
            if direction == "U":
                rope[0] = addX(rope[0], 1)
            elif direction == "D":
                rope[0] = addX(rope[0], -1)
            elif direction == "R":
                rope[0] = addY(rope[0], 1)
            elif direction == "L":
                rope[0] = addY(rope[0], -1)

            # Update rope
            for j in range(9):
                if abs(rope[j][0] - rope[j+1][0]) >= 2:
                    rope[j+1] = addX(rope[j+1], 1 if rope[j][0] > rope[j+1][0] else -1)
                    if abs(rope[j][1] - rope[j+1][1]) >= 1:
                        rope[j+1] = addY(rope[j+1], 1 if rope[j][1] > rope[j+1][1] else -1)

                elif abs(rope[j][1] - rope[j+1][1]) >= 2:
                    rope[j+1] = addY(rope[j+1], 1 if rope[j][1] > rope[j+1][1] else -1)
                    if abs(rope[j][0] - rope[j+1][0]) >= 1:
                        rope[j+1] = addX(rope[j+1], 1 if rope[j][0] > rope[j+1][0] else -1)

            if rope[9] not in visited_positions:
                visited_positions.append(rope[9])

    print(len(visited_positions))