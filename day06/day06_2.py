with open("input.txt") as file:
    input = list(reversed(file.read()))
    numberToMarker = 0
    marker=[]

    current = input.pop()
    while len(marker) < 14:
        if current in marker:
            marker = marker[marker.index(current) + 1:]
        marker.append(current)
            
        numberToMarker += 1
        current = input.pop()

    print(numberToMarker)
    
