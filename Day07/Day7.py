calculations = dict()
results = dict()

def parseCommand(command):
    (operation, result) = command.split('->')
    calculations[result.strip()] = operation.strip()

def calculate(value):
    #print "Running calculate(" + value + ")"
    try:
        return int(value)
    except ValueError:
        pass

    if value in results:
        return results[value]

    ops = calculations[value].split(' ')
    #print "in calculate, ops len = " + str(len(ops))
    if len(ops) == 1:
        result = calculate(ops[0])
    else:
        op = ops[-2]
        if op == 'AND':
            result = calculate(ops[0]) & calculate(ops[2])
        elif op == 'OR':
            result = calculate(ops[0]) | calculate(ops[2])
        elif op == 'RSHIFT':
            result = calculate(ops[0]) >> calculate(ops[2])
        elif op == 'LSHIFT':
            result = calculate(ops[0]) << calculate(ops[2])
        elif op == 'NOT':
            result = ~calculate(ops[1]) & 0xffff

    results[value] = result

    return results[value]



# with open("Day7TestInput.txt") as f:
#     for line in f.readlines():
#         parseCommand(line)
#
#     for k,v in calculations.items():
#         print k + ": " + v
#
#     for k in calculations.keys():
#         print k + " = " + str(calculate(k))

with open("Day7Input.txt") as f:
    for line in f.readlines():
        parseCommand(line)

    firstA = calculate('a')
    print firstA

    results = dict()
    results['b'] = firstA

    print calculate('a')
