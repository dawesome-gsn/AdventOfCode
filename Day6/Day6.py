import unittest
import re

lights = {}
for i in range(0, 1000):
    for j in range(0, 1000):
        lights[(i,j)] = 0

def NumLightsOn():
    return lights.values().count(True)

def TotalBrightness():
    return sum(lights.values())

def SwitchRange(start, end, command):
    (startX, startY) = start
    (endX, endY) = end
    for x in range(startX, endX + 1):
        for y in range(startY, endY + 1):
            if command == "turn on":
                lights[(x,y)] += 1
            elif command == "turn off":
                lights[(x,y)] -= 1
                if lights[(x,y)] < 0:
                    lights[(x,y)] = 0
            elif command == "toggle":
                lights[(x,y)] += 2
            else:
                print "Unexpected command"

def ParseDirection(direction):
    tuple = re.split('([0-9]*)', direction)
    #print tuple
    return tuple[0].strip(), (int(tuple[1]), int(tuple[3])), (int(tuple[5]), int(tuple[7]))

class TestDay6(unittest.TestCase):
    def testLights(self):
        self.assertEqual(0, NumLightsOn())
        SwitchRange((0,0), (999,999), "turn on")
        self.assertEqual(1000000, NumLightsOn())
        SwitchRange((0,0), (999,999), "turn off")
        self.assertEqual(0, NumLightsOn())
        SwitchRange((0,0), (999,0), "toggle")
        self.assertEqual(1000, NumLightsOn())
        SwitchRange((0,0), (499,0), "toggle")
        self.assertEqual(500, NumLightsOn())
        SwitchRange((0,0), (999,999), "turn on")
        SwitchRange((499,499), (500,500), "turn off")
        self.assertEqual(1000000 - 4, NumLightsOn())
        SwitchRange((0,0), (999,999), "turn off")

ParseDirection("turn on 0,0 through 999,999")
ParseDirection("turn off 499,499 through 500,500")
ParseDirection("toggle 0,0 through 999,0")

with open("Day6Input.txt") as f:
    directions = f.readlines()
    for direction in directions:
        command, first, second = ParseDirection(direction)
        #print command, first, second
        SwitchRange(first, second, command)
    print TotalBrightness()