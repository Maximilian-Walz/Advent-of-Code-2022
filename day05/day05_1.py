import re

with open("input.txt") as file:
    input = file.read()
    m = re.search(r'(?s)(.*)\n\n(.*)', input)
    crates = m.group(1)
    instructions = m.group(2)

    crates = crates.replace('[', ' ').replace(']', ' ').splitlines()
    crates = reversed(crates[:len(crates)-1])
    crates = [line[1::4] for line in crates]
    crates = [list(e) for e in zip(*crates)]
    crates = [[crate for crate in stack if crate != ' '] for stack in crates]

    for instruction in instructions.splitlines():
        m = re.search(r'move (.*) from (.*) to (.*)', instruction)
        amount = int(m.group(1))
        origin = int(m.group(2)) - 1
        destination = int(m.group(3)) - 1

        while amount > 0:
            crate = crates[origin].pop()
            crates[destination].append(crate)
            amount -= 1

    print(''.join([crate[-1] for crate in crates]))