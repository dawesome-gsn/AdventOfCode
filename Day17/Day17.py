import itertools

containers = list()

def numCombinations(containers, value):
    containers.sort()

    maxLength = len(containers)
    total = 0
    for i in range(len(containers)):
        total += containers[i]
        if total > value:
            maxLength = i
            break

    combinations = list()
    for i in range(1,maxLength + 1):
        combos = [list(x) for x in itertools.combinations(containers, i)]
        combinations.extend(combos)

    # print combinations
    winningCombinations = list()
    for combo in combinations:
        if sum(combo) == int(value):
            winningCombinations.append(combo)

    print len(winningCombinations)


with open("Test.txt") as f:
    for line in f.readlines():
        containers.append(int(line.strip()))

    numCombinations(containers, 25)

containers = list()
with open("Input.txt") as f:
    for line in f.readlines():
        containers.append(int(line.strip()))

    inp = list(map(int, open("Input.txt").read().splitlines()))

    q1 = 0
    q2 = 0
    for i in range(len(inp)-1):
        for perm in itertools.combinations(inp, i):
            if sum(perm) == 150:
                q1 += 1
        if q1 and not q2:
            q2 = q1
    print("Q1: {0}\nQ2: {1}".format(q1, q2))

    print sum(1 for size in range(len(containers)) for i in itertools.combinations(containers, size + 1) if sum(i) == 150)

    combinations = [c for i in xrange(1, len(containers)+1) for c in itertools.combinations(containers, i) if sum(c) == 150]
    print len(combinations)  # part1
    print len([c for c in combinations if len(c) == len(min(combinations, key=lambda x:len(x)))])
    numCombinations(containers, 150)