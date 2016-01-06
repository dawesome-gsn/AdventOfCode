import unittest

lights = {}
for i in range(0, 999):
    for j in range(0, 999):
        lights[(i,j)] = False

def NumLightsOn():
    return lights.values().count(True)

def SwitchRange(start, end, onOff):
    (startX, startY) = start
    (endX, endY) = end
    for x in range(startX, endX + 1):
        for y in range(startY, endY + 1):
            lights[(x,y)] = onOff


class TestDay6(unittest.TestCase):
    def testLights(self):
        self.assertEqual(0, NumLightsOn())
        SwitchRange((0,0), (999,999), True)
        self.assertEqual(1000000, NumLightsOn())

