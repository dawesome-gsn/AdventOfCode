import unittest

def contains3Vowels(input):
    return input.count('a') + input.count('e') + input.count('i') + input.count('o') + input.count('u') >= 3

def containsDoubleLetters(input):
    for i in range(0, len(input) - 1):
        if input[i] == input[i + 1]:
            return True

    return False

def containsRepeatedLetterWithSpacer(input):
    for i in range(0, len(input) - 2):
        if input[i] == input[i + 2]:
            return True
    return False

def containsRepeatedNonOverlappingPair(input):
    for i in range(0, len(input) - 3):
        if input[i:i+2] in input[i+2:]:
            return True
    return False

def containsForbiddenStrings(input):
    return 'ab' in input or 'cd' in input or 'pq' in input or 'xy' in input

def isNicePart1(input):
    return contains3Vowels(input) and containsDoubleLetters(input) and not containsForbiddenStrings(input)

def isNicePart2(input):
    return containsRepeatedLetterWithSpacer(input) and containsRepeatedNonOverlappingPair(input)

class TestDay5(unittest.TestCase):
    def testNice(self):
        self.assertEqual(True, isNicePart1('ugknbfddgicrmopn'))
        self.assertEqual(True, isNicePart1('aaa'))
        self.assertEqual(False, isNicePart1('jchzalrnumimnmhp'))
        self.assertEqual(False, isNicePart1('haegwjzuvuyypxyu'))
        self.assertEqual(False, isNicePart1('dvszwmarrgswjxmb'))
        self.assertEqual(True, isNicePart2('qjhvhtzxzkmpbjqj'))
        self.assertEqual(True, isNicePart2('xxyxx'))
        self.assertEqual(False, isNicePart2('uurcxstgmygtbstg'))
        self.assertEqual(False, isNicePart2('ieodomkazucvgmuy'))

with open('Day5Input.txt') as f:
    content = f.readlines()
    count = 0
    for s in content:
        if isNicePart2(s):
            count += 1
    print count
