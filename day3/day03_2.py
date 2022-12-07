def calcPriority(commonItem):
    if commonItem >= 65 and commonItem <= 90:
        return commonItem - 64 + 26
    elif commonItem >=97 and commonItem <= 122:
        return commonItem - 96

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

with open("input.txt") as file:
    priorities = 0
    for chunk in chunks(file.read().splitlines(), 3):
        commonItems = [item for item in chunk[0] if item in chunk[1] and item in chunk[2]]
        if len(commonItems) > 0:
            commonItem = ord(commonItems[0])
            priorities += calcPriority(commonItem)

    print(priorities)