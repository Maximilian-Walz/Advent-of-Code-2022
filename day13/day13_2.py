import json
import functools

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
    packages = [[[2]], [[6]]]
    for line in file:
        line = line.strip().replace("\n", "")
        if len(line) > 0:
            packages.append(json.loads(line))

    packages.sort(key=functools.cmp_to_key(compare))

    print((packages.index([[2]]) + 1) * (packages.index([[6]]) + 1))