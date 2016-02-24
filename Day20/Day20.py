import math

def divisors(houseNumber):
    firstHalf  = [i for i in xrange(1, int(math.sqrt(houseNumber)) +1) if houseNumber % i == 0]
    secondHalf = [houseNumber / i for i in firstHalf if houseNumber != i * i]
    return firstHalf + secondHalf

def numPresents(divs):
    return sum(divs) * 10

def numPresentsPart2(divs, houseNumber):
    return sum([d for d in divs if (houseNumber / d) < 50]) * 11

for i in range(1, 10):
    print "House " + str(i) + " has " + str(numPresents(divisors(i)))

part1Ans = None
part2Ans = None
targetGiftLevel = 36000000
i = 2
while not part1Ans or not part2Ans:
    divs = divisors(i)
    if not part1Ans:
        if numPresents(divs) >= targetGiftLevel:
            part1Ans = i
    if not part2Ans:
        if numPresentsPart2(divs, i) >= targetGiftLevel:
            part2Ans = i
    i += 1

print "Part 1: " + str(part1Ans)
print "Part 2: " + str(part2Ans)
#776160 is too low for part2?

