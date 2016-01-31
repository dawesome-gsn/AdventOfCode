import re

sues = dict()
facts = dict()

def parseSue(line):
    mo = re.match("Sue ([0-9]*):", line)
    sueNumber = mo.group(1)
    sues[sueNumber] = dict()

    mo = re.match(".*children: ([0-9]*)", line)
    if mo:
        sues[sueNumber]["children"] = int(mo.group(1))

    mo = re.match(".*cats: ([0-9]*)", line)
    if mo:
        sues[sueNumber]["cats"] = int(mo.group(1))

    mo = re.match(".*samoyeds: ([0-9]*)", line)
    if mo:
        sues[sueNumber]["samoyeds"] = int(mo.group(1))

    mo = re.match(".*pomeranians: ([0-9]*)", line)
    if mo:
        sues[sueNumber]["pomeranians"] = int(mo.group(1))

    mo = re.match(".*akitas: ([0-9]*)", line)
    if mo:
        sues[sueNumber]["akitas"] = int(mo.group(1))

    mo = re.match(".*vizslas: ([0-9]*)", line)
    if mo:
        sues[sueNumber]["vizslas"] = int(mo.group(1))

    mo = re.match(".*goldfish: ([0-9]*)", line)
    if mo:
        sues[sueNumber]["goldfish"] = int(mo.group(1))

    mo = re.match(".*trees: ([0-9]*)", line)
    if mo:
        sues[sueNumber]["trees"] = int(mo.group(1))

    mo = re.match(".*cars: ([0-9]*)", line)
    if mo:
        sues[sueNumber]["cars"] = int(mo.group(1))

    mo = re.match(".*perfumes: ([0-9]*)", line)
    if mo:
        sues[sueNumber]["perfumes"] = int(mo.group(1))


def parseFacts(line):
    name, amount = line.split(": ")
    facts[name.strip()] = int(amount.strip())

with open("SueInput.txt") as s:
    for line in s.readlines():
        parseSue(line)

with open("SueFacts.txt") as s:
    for line in s.readlines():
        parseFacts(line)

    # print information on our aunt Sues
    # for k, v in sues.iteritems():
    #     print k + ": "
    #     for attribute, amount in v.iteritems():
    #         print attribute + ": " + amount

    # print known Aunt Sue facts
    for k, v in facts.iteritems():
        print k + ": " + str(v)


loopMatchingSues = dict()
for k in sues:
    match = True
    for fact in facts:
        #make it explicit what we're dealing with
        factAttribute = fact
        factAmount = facts[fact]

        if factAttribute in sues[k].keys():
            if factAttribute == "cats" or factAttribute == "trees":
                if factAmount >= sues[k][factAttribute]:
                    match = False
            elif factAttribute == "pomeranians" or factAttribute == "goldfish":
                if factAmount <= sues[k][factAttribute]:
                    match = False
            elif factAmount != sues[k][factAttribute]:
                match = False
    if match:
        loopMatchingSues[k] = sues[k]

print len(loopMatchingSues)
for k in loopMatchingSues:
    print k, loopMatchingSues[k]