import re

totalOriginalCodeChars = 0
totalEncodedCodeChars = 0
stringChars = 0

hexidecimalMatch = re.compile("\\\\x[0-9A-Fa-f][0-9A-Fa-f]")


def decode(line):
    convertedLine = line.replace("\\\\", "B")  # replace \\ with 1 character
    convertedLine = convertedLine.replace("\\\"", '"')
    # print strippedline
    convertedLine = re.sub(hexidecimalMatch, "A", convertedLine)
    lineStringChars = len(convertedLine)

    return lineStringChars

def encode(line):
    encodedLine = line

    #print "encoded line = " + encodedLine
    encodedLine = encodedLine.replace("\\", "\\\\")
    #print "after first replace = " + encodedLine
    encodedLine = encodedLine.replace("\"", "\\\"")
    #print "after second replace = " + encodedLine

    #print line, encodedLine, len(encodedLine) + 2
    return encodedLine, len(encodedLine) + 2 #plus 2 for the outside quotes

#with open("Day8TestInput.txt") as f:
with open("Day8Input.txt") as f:
    for line in f.readlines():
        strippedLine = line.strip()
        lineCodeChars = len(strippedLine)

        noQuotesLine = strippedLine[1:-1]
        print "noQuotesLine = " + noQuotesLine
        encodedLine, encodedLineCodeChars = encode(strippedLine)

        # strip the quotes from the outside
        lineStringChars = decode(noQuotesLine)

        print strippedLine, lineCodeChars, lineStringChars
        print encodedLine, encodedLineCodeChars

        stringChars += lineStringChars
        totalOriginalCodeChars += lineCodeChars
        totalEncodedCodeChars += encodedLineCodeChars


    print stringChars, totalOriginalCodeChars, totalEncodedCodeChars
    print totalOriginalCodeChars - stringChars
    print totalEncodedCodeChars - totalOriginalCodeChars
