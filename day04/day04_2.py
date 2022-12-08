with open("input.txt") as file:
    count = 0
    for line in file.read().splitlines():
        pair = line.split(",")

        lower1 = int(pair[0].split("-")[0])
        lower2 = int(pair[1].split("-")[0])
        upper1 = int(pair[0].split("-")[1])
        upper2 = int(pair[1].split("-")[1])

        if len([i for i in range(lower1, upper1+1) if i in range(lower2, upper2+1)]) > 0:
            count += 1

    print(count)

        