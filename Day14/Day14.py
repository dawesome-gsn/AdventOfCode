deers = list()

class Reindeer:
    name = ""
    speed = 0
    rate = 0
    rest = 0
    points = 0

    def __init__(self, name, speed, rate, rest):
        self.name = name
        self.speed = speed
        self.rate = rate
        self.rest = rest

    def distance(self, time):
        distance = 0
        while time > 0:
            distance += self.speed * min(time, self.rate)
            time -= self.rate
            time -= self.rest
        return distance



def parseline(line):
    name, line = line.split(" can fly ")
    speed, line = line.split(" km/s for ")
    rate, line = line.split(" seconds, but then must rest for ")
    rest, line = line.split(" seconds.")
    deers.append(Reindeer(name, int(speed), int(rate), int(rest)))

with open("Input.txt") as f:
#with open("TestInput.txt") as f:
    for line in f.readlines():
        parseline(line)

    maxDistance = 0
    for item in deers:
        maxDistance = max(maxDistance, item.distance(2503))
    print maxDistance

    for i in range(1,2504):
        currentLeadDeer = list()
        currentMaxDistance = 0
        for deer in deers:
            deerDistance = deer.distance(i)
            if deerDistance > currentMaxDistance:
                currentLeadDeer = list()
                currentLeadDeer.append(deer)
                currentMaxDistance = deerDistance
            elif deerDistance == currentMaxDistance:
                currentLeadDeer.append(deer)

        for deer in currentLeadDeer:
            deer.points += 1

    for deer in deers:
        print deer.name, deer.points