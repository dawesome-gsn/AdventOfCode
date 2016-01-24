def LookAndSay(sequence):
    newSequence = ""
    currentChar = ""
    currentCount = 0

    for char in sequence:
        if char != currentChar:
            if currentCount > 0:
                newSequence += (str(currentCount))
                newSequence += (currentChar)
            currentChar = char
            currentCount = 1
        else:
            currentCount += 1

    newSequence += (str(currentCount))
    newSequence += (currentChar)

    return newSequence


print LookAndSay("1")
print LookAndSay("11")
print LookAndSay("21")
print LookAndSay("1211")
print LookAndSay("111221")

nextSequence = "1113122113"
for i in range(50):
    nextSequence = LookAndSay(nextSequence)

print nextSequence
print len(nextSequence)