import itertools
import sys

guests = dict()

def parseLine(line, guests):
    person, rest = line.split(" would ")
    amount, otherPerson = rest.split(" happiness units by sitting next to ")

    #remove the period from otherPerson
    otherPerson = otherPerson[0:-2]
    if amount[:4] == 'gain':
        amount = int(amount[5:])
    else:
        amount = -int(amount[5:])

    if not guests.has_key(person):
        guests[person] = dict()
    guests[person][otherPerson] = amount

#with open("TestInput.txt") as f:
with open("Input.txt") as f:
    for line in f.readlines():
        parseLine(line, guests)
    print guests

    guests["me"] = dict()
    for person in guests.keys():
        if person != "me":
            guests[person]["me"] = 0
            guests["me"][person] = 0

    allSeatingArrangements = list(itertools.permutations(guests.keys()))

    bestHappiness = -sys.maxsize - 1
    print(allSeatingArrangements)
    for seats in allSeatingArrangements:
        currentHappiness = 0
        for i in range(len(seats)):
            currentHappiness += guests[seats[i]][seats[(i+1) % len(seats)]]
            currentHappiness += guests[seats[i]][seats[(i-1) % len(seats)]]
        bestHappiness = max(bestHappiness, currentHappiness)

    print bestHappiness