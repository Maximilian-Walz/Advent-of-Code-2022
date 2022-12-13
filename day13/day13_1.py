import json

def compare(left, right):
    if type(left) == type(right) == int:
        if left < right:
            return -1
        elif left > right:
            return 1
        else:
            return 0

    if type(left) != list:
        left = [left]
    if type(right) != list:
        right = [right]

    for i in range(len(left)):
        if i >= len(right):
            # Right run out of elements
            return 1
        comparison = compare(left[i], right[i])
        if comparison == 0:
            # Not clear, check next element
            continue
        return comparison
    if len(left) == len(right):
       # All elements are equal
        return 0
    # Left run out of elements
    return -1
         


with open("input.txt") as file:
    pairs = [pair.split("\n") for pair in file.read().split("\n\n")]

    index_sum = 0
    for i, pair in enumerate(pairs):
        left = json.loads(pair[0])
        right = json.loads(pair[1])

        if(compare(left, right) == -1):
            index_sum += i + 1

    print(index_sum)



