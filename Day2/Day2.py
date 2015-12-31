__author__ = 'mdawe'

import unittest
import Utils
import os

class Day2:
    def Area(self, length, width, height):
        return 2*length*width + 2*width*height + 2*height*length

    def Slack(self, length, width, height):
        return min(length * width, width * height, length * height)

    def WrappingNeeded(self, length, width, height):
        return self.Area(length, width, height) + self.Slack(length, width, height)


class TestDay2(unittest.TestCase):
    def testArea(self):
        d = Day2()
        self.assertEqual(d.Area(2,3,4), 52)
        self.assertEqual(d.Area(1,1,10), 42)

    def testSlack(self):
        d = Day2()
        self.assertEqual(d.Slack(2,3,4), 6)
        self.assertEqual(d.Slack(1,1,10), 1)

    def test1(self):
        d = Day2()
        self.assertEqual(d.WrappingNeeded(2,3,4), 58)
        self.assertEqual(d.WrappingNeeded(1,1,10), 43)

if __name__ == '__main__':
    d = Day2()

    total = 0

    f = open('Day2Input.txt')
    for line in f:
        l,w,h = line.split('x')
        l,w,h = int(l), int(w), int(h)
        total += d.WrappingNeeded(l,w,h)

    print total
