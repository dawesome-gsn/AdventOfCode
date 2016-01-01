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

    def Fly(self, str, useRoboSanta):
        coord_list.clear()
        coord_list.add((0,0))

        for char in str:
            if char == '<':
                self.currentPos.x += -1
            elif char == '>':
                self.currentPos.x += 1
            elif char == '^':
                self.currentPos.y += 1
            elif char == 'v':
                self.currentPos.y += -1
            coord_list.add((self.currentPos.x, self.currentPos.y))

    def NumHouses(self, str, useRoboSanta=False):
        self.Fly(str, useRoboSanta)
        return len(coord_list)


class TestDay3(unittest.TestCase):
    def testFly(self):
        d = Day3()
        self.assertEqual(d.NumHouses('>'), 2)
        d = Day3()
        self.assertEqual(d.NumHouses('^>v<'), 4)
        d = Day3()
        self.assertEqual(d.NumHouses('^v^v^v^v^v'), 2)

if __name__ == '__main__':
    #unittest.main()
    d = Day3()
    full_path = os.path.realpath(__file__)
    file_path = '%s/Day3Input.txt' % os.path.dirname(full_path)

    with open(file_path) as f:
        s = f.read()
        print d.NumHouses(s)