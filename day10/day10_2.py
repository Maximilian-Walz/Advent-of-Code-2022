with open("input.txt") as file:
    total_signal_strength = 0

    clock = 0
    busy = 0
    x = 1

    line = file.readline()
    while line:
        clock += 1
        # start of cycle 
                    
        # print to CRT screen
        col = (clock-1) % 40
        if abs(x - col) <= 1:
            print("#", end="")
        else:
            print(".", end="")
        if col == 39:
            print()

        # execute line
        if line.strip() == "noop":
            line = file.readline()
        else:
            if busy < 1:
                busy += 1
            else:   
                x += int(line.strip().split(" ")[1])
                busy = 0
                line = file.readline()