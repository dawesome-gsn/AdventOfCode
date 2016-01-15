import re

codeChars = 0
stringChars = 0

hexidecimalMatch = re.compile("\\\\x[0-9A-Fa-f][0-9A-Fa-f]")

with open("Day8Input.txt") as f:
    for line in f.readlines():
        lineCodeChars = 0
        lineStringChars = 0

        strippedLine = line.strip()

        lineStringChars = len(strippedLine)
        stringChars += lineStringChars

        #strip the quotes from the outside
        strippedLine = strippedLine[1:-1]
        convertedLine = strippedLine.replace("\\\\", "B") #replace \\ with 1 character
        convertedLine = convertedLine.replace("\\\"",'"')
        #print strippedLine
        convertedLine = re.sub(hexidecimalMatch, "A", convertedLine)
        lineCodeChars = len(convertedLine)

        #splitLine = strippedLine.split("\\")
        # for item in splitLine:
        #     #print item
        #     lineCodeChars += len(item)
        #     # if len(item) > 0 and item[0] == 'x' and hexidecimalMatch.match(item[1:]):
        #     #     lineCodeChars -= 2
        codeChars += lineCodeChars

        print line.strip()
        print convertedLine, lineStringChars,lineCodeChars
        print

    print stringChars, codeChars
    print stringChars - codeChars
