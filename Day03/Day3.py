__author__ = 'mdawe'

import unittest
import os

coord_list = set()

class Position:
    def __init__(self):
        self.x = 0
        self.y = 0

class Day3:
    def __init__(self):
        self.currentPos = Position()
        self.positions = set()
        self.positions.add(self.currentPos)

    def Fly(self, directions, useRoboSanta):
        roboTurn = False
        santa = Position()
        roboSanta = Position()

        coord_list.clear()
        coord_list.add((0,0))

        print "useRoboSanta = " + str(useRoboSanta)

        for char in directions:
            self.currentPos = santa
            if useRoboSanta and roboTurn:
                self.currentPos = roboSanta

            if char == '<':
                self.currentPos.x += -1
            elif char == '>':
                self.currentPos.x += 1
            elif char == '^':
                self.currentPos.y += 1
            elif char == 'v':
                self.currentPos.y += -1
            coord_list.add((self.currentPos.x, self.currentPos.y))

            if useRoboSanta and roboTurn:
                roboSanta.x = self.currentPos.x
                roboSanta.y = self.currentPos.y
            else:
                santa.x = self.currentPos.x
                santa.y = self.currentPos.y

            print "Santa at " + str(santa.x) + ", " + str(santa.y)
            print "RoboS at " + str(roboSanta.x) + ", " + str(roboSanta.y)

            roboTurn = not roboTurn

    def NumHouses(self, directions, useRoboSanta=False):
        self.Fly(directions, useRoboSanta)
        return len(coord_list)


class TestDay3(unittest.TestCase):
    def testFly(self):
        d = Day3()
        self.assertEqual(d.NumHouses('>'), 2)
        d = Day3()
        self.assertEqual(d.NumHouses('^>v<'), 4)
        d = Day3()
        self.assertEqual(d.NumHouses('^v^v^v^v^v'), 2)
        d = Day3()
        self.assertEqual(d.NumHouses('^v', True), 3)
        d = Day3()
        self.assertEqual(d.NumHouses('^>v<', True), 3)
        d = Day3()
        self.assertEqual(d.NumHouses('^v^v^v^v^v', True), 11)

if __name__ == '__main__':
    #unittest.main()
    d = Day3()
    full_path = os.path.realpath(__file__)
    file_path = '%s/Day3Input.txt' % os.path.dirname(full_path)

    with open(file_path) as f:
        s = f.read()
        print "Santa houses = " + str(d.NumHouses(s, False))
        print "With RoboSanta = " + str(d.NumHouses(s, True))