def neighborsOn(x,y,lights):
    on = 0
    neighbors = list()
    for nX in range(x-1 if x>0 else x, x+2 if x<len(lights[x])-1 else x+1):
        for nY in range(y-1 if y>0 else y, y+2 if y<len(lights)-1 else y+1):
            if nX != x or nY != y:
                neighbors.append(lights[nX][nY])
    # for item in neighbors:
    #     print item
    return neighbors.count('#')

def step(lights, nextLights):
    nextLights = [['.' for x in range(6)] for x in range(6)]
    for x in range(6):
        for y in range(6):
            num = neighborsOn(x, y, lights)
            if lights[x][y] == '.' and num == 3:
                nextLights[x][y] = '#'
            if lights[x][y] == '#':
                if num == 2 or num == 3:
                    nextLights[x][y] = '#'
    return nextLights

lights = [['.' for x in range(6)] for x in range(6)]
nextLights = ''

lights[0][1] = lights[0][3] = lights[0][5] = '#'
lights[1][3] = lights[1][4] = '#'
lights[2][0] = lights[2][5] = '#'
lights[3][2] = '#'
lights[4][0] = lights[4][2] = lights[4][5] = '#'
lights[5][0] = lights[5][1] = lights[5][2] = lights[5][3] = '#'

# print neighborsOn(0,0, lights)
# print neighborsOn(5,5, lights)
# print neighborsOn(0,4, lights)

for x in range(4):
    lights = step(lights, nextLights)

for x in lights:
    print x
print sum(x.count('#') for x in lights)
