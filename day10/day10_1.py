with open("input.txt") as file:
    total_signal_strength = 0

    clock = 0
    busy = 0
    x = 1

    line = file.readline()
    while line:
        clock += 1
        # start of cycle 
        print(f"Start of cycle: {clock} - {line.strip()} - Busy: {busy} - X: {x}")
        if (clock - 20) % 40 == 0:
            print(f"{clock}!!{x}")
            total_signal_strength += x * clock
            
        if line.strip() == "noop":
            line = file.readline()
        else:
            if busy < 1:
                busy += 1
            else:   
                x += int(line.strip().split(" ")[1])
                busy = 0
                line = file.readline()


    print(total_signal_strength)