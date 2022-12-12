def addX(tuple, value):
    return (tuple[0] + value, tuple[1])

def addY(tuple, value):
    return (tuple[0], tuple[1] + value)

with open("input.txt") as file:
    head = (0, 0)
    tail = (0, 0)
    visited_positions = [tail]

    for line in file.readlines():
        direction = line.split(" ")[0]
        distance = int(line.split(" ")[1])


        for i in range(distance):
            if direction == "U":
                head = addX(head, 1)
            elif direction == "D":
                head = addX(head, -1)
            elif direction == "R":
                head = addY(head, 1)
            elif direction == "L":
                head = addY(head, -1)

            # Update tail
            if abs(head[0] - tail[0]) >= 2:
                tail = addX(tail, 1 if head[0] > tail[0] else -1)
                if abs(head[1] - tail[1]) >= 1:
                    tail = addY(tail, 1 if head[1] > tail[1] else -1)

            elif abs(head[1] - tail[1]) >= 2:
                tail = addY(tail, 1 if head[1] > tail[1] else -1)
                if abs(head[0] - tail[0]) >= 1:
                    tail = addX(tail, 1 if head[0] > tail[0] else -1)

            if tail not in visited_positions:
                visited_positions.append(tail)

    print(len(visited_positions))