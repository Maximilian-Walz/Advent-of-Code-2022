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
    readings = []
    beacons = []
    for line in file.readlines():
        groups = re.search(r'Sensor at x=(-?\d*), y=(-?\d*): closest beacon is at x=(-?\d*), y=(-?\d*)', line).groups()
        readings.append({"x": int(groups[0]), "y": int(groups[1]), "influence": distance((int(groups[0]), int(groups[1])), (int(groups[2]), int(groups[3])))})
        beacons.append((int(groups[2]), int(groups[3])))

    def getRelevantInterval(y):
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
        return relevantIntervals

    def printScore(x, y):
        print(x * 4000000 + y)

    for i in range(4000001):
        intervals = getRelevantInterval(i)
        if len(intervals) == 1:
            if intervals[0][0] <= 0 and intervals[0][1] >= 4000000: # If it spans the entire area, there is no free spot
                continue
            elif intervals[0][0] > 0:
                printScore(0, i) # Needs to be 0 bescore the location is unique
            else:
                printScore(4000000, i) # Needs to be 4000000 because the location is unique
        else: # There have to be two intervals
            printScore(intervals[0][1] + 1, i) # The unique free spot is between the two intervals
        break


    



