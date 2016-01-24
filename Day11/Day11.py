import re

def containsIOL(password):
    return 'i' in password or 'l' in password or 'o' in password

def hasRepeatedLetters(password):
    repeatedLettersRe = re.compile(r'((\w)\2)')
    matches = re.findall(repeatedLettersRe, password)
    #for match in matches:
       #print match.group()
    return len(matches) >= 2

def containsStraight(password):
    for i in range(len(password)-2):
        if ord(password[i]) == ord(password[i+1]) - 1 and ord(password[i+1]) == ord(password[i+2]) - 1:
            return True
    return False

def validPassword(password):
    return not containsIOL(password) and hasRepeatedLetters(password) and containsStraight(password)

def incrementPassword(password):
    newPassword = password[::-1] #reverse the string
    #print "incrementPassword, " + newPassword
    for i in range(0, len(newPassword)):
        first = last = ""
        if i > 0:
            first = newPassword[0:i]
            # print "first: " + first

        if i < len(newPassword) - 1:
            last = newPassword[i+1:]
            # print "last: " + last

        if newPassword[i] == 'z':
            newPassword = first + 'a' + last
            # print "replaced z, newPassword = " + newPassword
        else:
            # print "doing increment"
            # print newPassword[0:i-1]
            # print chr(ord(newPassword[i]) + 1)

            newPassword = first + (chr(ord(newPassword[i]) + 1)) + last
            # print "end increment: " + newPassword
            break


    return newPassword[::-1]

# print hasRepeatedLetters("hijklmmn")
# print hasRepeatedLetters("abbceffg")
# print containsStraight("hijklmmn")
# print containsStraight("abbceffg")
# print validPassword("hijklmmn")
# print validPassword("abbcegjk")
# print validPassword("abcdffaa")
# print incrementPassword('xx')
#print incrementPassword('xy')
#print incrementPassword('xz')
password = "cqjxjnds"
while not validPassword(password):
    password = incrementPassword(password)
print password
password = incrementPassword(password)
while not validPassword(password):
    password = incrementPassword(password)
print password
