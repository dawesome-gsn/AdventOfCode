import hashlib

def find5Zeros(input):
    count = 0
    while True:
        count += 1
        #print count
        m = hashlib.md5()
        m.update(input + str(count))
        output = m.hexdigest()
        #print output
        if output[:6] == '000000':
            return count


print find5Zeros('yzbqklnj')
