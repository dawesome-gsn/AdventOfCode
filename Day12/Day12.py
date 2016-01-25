import json

santaJson = ""
total = 0


def returnNumber(obj, runningTotal):
    if isinstance(obj, dict):
        if obj.has_key("red") or "red" in obj.values():
            pass
        else:
            runningTotal = returnNumber(obj.values(), runningTotal)
    elif isinstance(obj, list):
        for item in obj:
            try:
                runningTotal += int(item)
            except TypeError:
                runningTotal = returnNumber(item, runningTotal)
            except ValueError:
                pass
    else:
        print "something else here: " + obj
    return runningTotal

with open("Day12Test.txt") as f:
    testJsonList = list()
    for line in f.readlines():
        testJsonList.append(json.loads(line.strip()))

    for entry in testJsonList:
        print returnNumber(entry, 0)

with open("Day12Input.txt") as f:
    santaJson = json.load(f)
    print santaJson


for e in santaJson:
    total = returnNumber(santaJson[e], total)

print total