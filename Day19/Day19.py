import string
replacements = dict()
nextMolecules = set()

def parseInputLine(line):
    first, second = line.split(" => ")
    first = first.strip()
    second = second.strip()

    if not replacements.has_key(first):
        replacements[first] = list()
    replacements[first].append(second)

def nextStep(input):
    for letterIter in range(0, len(input)):
        key = input[letterIter]
        if key in string.lowercase and key != 'e':
            continue

        if not letterIter == len(input) - 1:
            lookaheadLetter = input[letterIter + 1]
            if lookaheadLetter in string.lowercase:
                key += lookaheadLetter

        if key in replacements.keys():
            for replaceValue in replacements[key]:
                newMolecule = input[0:letterIter]
                newMolecule += replaceValue
                newMolecule += input[letterIter+len(key):]
                # print "newMolecule = ", newMolecule
                nextMolecules.add(newMolecule)
    return nextMolecules

#with open("TestInput.txt") as f:
with open("Input.txt") as f:
    for line in f.readlines():
        parseInputLine(line)

    # for k, v in replacements.iteritems():
    #     print k, v

targeMolecule = "CRnCaCaCaSiRnBPTiMgArSiRnSiRnMgArSiRnCaFArTiTiBSiThFYCaFArCaCaSiThCaPBSiThSiThCaCaPTiRnPBSiThRnFArArCaCaSiThCaSiThSiRnMgArCaPTiBPRnFArSiThCaSiRnFArBCaSiRnCaPRnFArPMgYCaFArCaPTiTiTiBPBSiThCaPTiBPBSiRnFArBPBSiRnCaFArBPRnSiRnFArRnSiRnBFArCaFArCaCaCaSiThSiThCaCaPBPTiTiRnFArCaPTiBSiAlArPBCaCaCaCaCaSiRnMgArCaSiThFArThCaSiThCaSiRnCaFYCaSiRnFYFArFArCaSiRnFYFArCaSiRnBPMgArSiThPRnFArCaSiRnFArTiRnSiRnFYFArCaSiRnBFArCaSiRnTiMgArSiThCaSiThCaFArPRnFArSiRnFArTiTiTiTiBCaCaSiRnCaCaFYFArSiThCaPTiBPTiBCaSiThSiRnMgArCaF"
#nextMolecules = nextStep("HSiSO")
nextMolecules = nextStep(targeMolecule)
for i in nextMolecules:
    print i
print len(nextMolecules)


