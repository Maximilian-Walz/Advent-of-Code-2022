with open("input.txt") as file:
    priorities = 0
    for line in file.read().splitlines():
        fstHalf = line[0:int(len(line)/2)]
        sndHalf = line[int(len(line)/2): int(len(line))]
        commonItems = [item for item in sndHalf if item in fstHalf]

        if len(commonItems) > 0:
            commonItem = ord(commonItems[0])
            if commonItem >= 65 and commonItem <= 90:
                priorities += commonItem - 64 + 26
            elif commonItem >=97 and commonItem <= 122:
                priorities += commonItem - 96

    print(priorities)