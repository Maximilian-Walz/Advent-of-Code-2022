import re

def distance(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

def influenceInterval(reading, target_y):
    influenceWidth = reading["influence"] - abs(target_y - reading["y"])
    if influenceWidth < 0:
        return (0, -1)
    return (reading["x"] - influenceWidth, reading["x"] + influenceWidth)

def contains(interval, x):
    return interval[0] <= x <= interval[1]

with open("input.txt") as file:
    y = 2000000
    readings = []
    beacons = []
    for line in file.readlines():
        groups = re.search(r'Sensor at x=(-?\d*), y=(-?\d*): closest beacon is at x=(-?\d*), y=(-?\d*)', line).groups()
        readings.append({"x": int(groups[0]), "y": int(groups[1]), "influence": distance((int(groups[0]), int(groups[1])), (int(groups[2]), int(groups[3])))})
        beacons.append((int(groups[2]), int(groups[3])))

    influenceIntervals = sorted([interval for interval in [influenceInterval(reading, y) for reading in readings] if interval[1] - interval[0] >= 0], key=lambda x: x[0])

    relevantIntervals = []
    for interval in influenceIntervals:
        contained = -1
        for i, relevantInterval in enumerate(relevantIntervals):
            if contains(relevantInterval, interval[0]):
                contained = i
                break
        if contained >= 0:
            relevantIntervals[i] = (relevantInterval[0] , max(relevantInterval[1], interval[1]))
        else:
            relevantIntervals.append(interval)

    coveredPositions = sum([interval[1] - interval[0] + 1 for interval in relevantIntervals])

    for beacon in set(beacons):
        for interval in relevantIntervals:
            if beacon[1] == y and contains(interval, beacon[0]):
                coveredPositions -= 1
                break

    print(coveredPositions)    
    



